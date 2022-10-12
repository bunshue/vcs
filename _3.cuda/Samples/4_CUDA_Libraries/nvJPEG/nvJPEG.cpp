// This sample needs at least CUDA 10.0. It demonstrates usages of the nvJPEG
// library nvJPEG supports single and multiple image(batched) decode. Multiple
// images can be decoded using the API for batch mode

#include <cuda_runtime_api.h>
#include "helper_nvJPEG.hxx"

int dev_malloc(void** p, size_t s) { return (int)cudaMalloc(p, s); }

int dev_free(void* p) { return (int)cudaFree(p); }

int host_malloc(void** p, size_t s, unsigned int f) { return (int)cudaHostAlloc(p, s, f); }

int host_free(void* p) { return (int)cudaFreeHost(p); }

typedef std::vector<std::string> FileNames;
typedef std::vector<std::vector<char> > FileData;

struct decode_params_t
{
    std::string input_dir;
    int batch_size;
    int total_images;
    int dev;
    int warmup;

    nvjpegJpegState_t nvjpeg_state;
    nvjpegHandle_t nvjpeg_handle;
    cudaStream_t stream;

    // used with decoupled API
    nvjpegJpegState_t nvjpeg_decoupled_state;
    nvjpegBufferPinned_t pinned_buffers[2]; // 2 buffers for pipelining
    nvjpegBufferDevice_t device_buffer;
    nvjpegJpegStream_t  jpeg_streams[2]; //  2 streams for pipelining
    nvjpegDecodeParams_t nvjpeg_decode_params;
    nvjpegJpegDecoder_t nvjpeg_decoder;

    nvjpegOutputFormat_t fmt;
    bool write_decoded;
    std::string output_dir;

    bool pipelined;
    bool batched;
};

int read_next_batch(FileNames& image_names, int batch_size, FileNames::iterator& cur_iter, FileData& raw_data, std::vector<size_t>& raw_len, FileNames& current_names)
{
    int counter = 0;

    while (counter < batch_size)
    {
        if (cur_iter == image_names.end())
        {
            std::cerr << "Image list is too short to fill the batch, adding files from the beginning of the image list" << std::endl;
            cur_iter = image_names.begin();
        }

        if (image_names.size() == 0)
        {
            std::cerr << "No valid images left in the input list, exit" << std::endl;
            return EXIT_FAILURE;
        }

        // Read an image from disk.
        std::ifstream input(cur_iter->c_str(), std::ios::in | std::ios::binary | std::ios::ate);
        if (!(input.is_open()))
        {
            std::cerr << "Cannot open image: " << *cur_iter << ", removing it from image list" << std::endl;
            image_names.erase(cur_iter);
            continue;
        }

        // Get the size
        std::streamsize file_size = input.tellg();
        input.seekg(0, std::ios::beg);
        // resize if buffer is too small
        if (raw_data[counter].size() < file_size)
        {
            raw_data[counter].resize(file_size);
        }
        if (!input.read(raw_data[counter].data(), file_size))
        {
            std::cerr << "Cannot read from file: " << *cur_iter << ", removing it from image list" << std::endl;
            image_names.erase(cur_iter);
            continue;
        }
        raw_len[counter] = file_size;

        current_names[counter] = *cur_iter;

        counter++;
        cur_iter++;
    }
    return EXIT_SUCCESS;
}

// prepare buffers for RGBi output format
int prepare_buffers(FileData& file_data, std::vector<size_t>& file_len, std::vector<int>& img_width, std::vector<int>& img_height, std::vector<nvjpegImage_t>& ibuf,
    std::vector<nvjpegImage_t>& isz, FileNames& current_names, decode_params_t& params)
{
    int widths[NVJPEG_MAX_COMPONENT];
    int heights[NVJPEG_MAX_COMPONENT];
    int channels;
    nvjpegChromaSubsampling_t subsampling;

    for (int i = 0; i < file_data.size(); i++)
    {
        std::cout << "prepare_buffers, i = " << i << ", filename = " << current_names[i] << std::endl;

        checkCudaErrors(nvjpegGetImageInfo(params.nvjpeg_handle, (unsigned char*)file_data[i].data(), file_len[i], &channels, &subsampling, widths, heights));

        img_width[i] = widths[0];
        img_height[i] = heights[0];

        //printf("Processing: %s, %d channels\n", current_names[i], channels);

        std::cout << "Ū���ɮ� : " << current_names[i] << std::endl;
        std::cout << "Image is " << channels << " channels." << std::endl;
        for (int c = 0; c < channels; c++)
        {
            std::cout << "Channel #" << c << " size: " << widths[c] << " x " << heights[c] << std::endl;
        }

        printf("subsampling : %d\n", subsampling);

        switch (subsampling)
        {
        case NVJPEG_CSS_444:
            std::cout << "YUV 4:4:4 chroma subsampling" << std::endl;
            break;
        case NVJPEG_CSS_440:
            std::cout << "YUV 4:4:0 chroma subsampling" << std::endl;
            break;
        case NVJPEG_CSS_422:
            std::cout << "YUV 4:2:2 chroma subsampling" << std::endl;
            break;
        case NVJPEG_CSS_420:
            std::cout << "YUV 4:2:0 chroma subsampling" << std::endl;
            break;
        case NVJPEG_CSS_411:
            std::cout << "YUV 4:1:1 chroma subsampling" << std::endl;
            break;
        case NVJPEG_CSS_410:
            std::cout << "YUV 4:1:0 chroma subsampling" << std::endl;
            break;
        case NVJPEG_CSS_GRAY:
            std::cout << "Grayscale JPEG " << std::endl;
            break;
        case NVJPEG_CSS_UNKNOWN:
            std::cout << "Unknown chroma subsampling" << std::endl;
            return EXIT_FAILURE;
        }

        int mul = 1;
        // in the case of interleaved RGB output, write only to single channel, but
        // 3 samples at once
        if (params.fmt == NVJPEG_OUTPUT_RGBI || params.fmt == NVJPEG_OUTPUT_BGRI)
        {
            printf("XXXXXXXXXXX 111\n");
            channels = 1;
            mul = 3;
        }
        // in the case of rgb create 3 buffers with sizes of original image
        else if (params.fmt == NVJPEG_OUTPUT_RGB || params.fmt == NVJPEG_OUTPUT_BGR)
        {
            printf("222\n");
            channels = 3;
            widths[1] = widths[2] = widths[0];
            heights[1] = heights[2] = heights[0];
        }

        printf("channels = %d\n", channels);

        // realloc output buffer if required
        for (int c = 0; c < channels; c++)
        {
            int aw = mul * widths[c];
            int ah = heights[c];
            int sz = aw * ah;
            ibuf[i].pitch[c] = aw;
            if (sz > isz[i].pitch[c])
            {
                if (ibuf[i].channel[c])
                {
                    checkCudaErrors(cudaFree(ibuf[i].channel[c]));
                }
                checkCudaErrors(cudaMalloc(&ibuf[i].channel[c], sz));
                isz[i].pitch[c] = sz;
            }
        }
    }
    return EXIT_SUCCESS;
}

void create_decoupled_api_handles(decode_params_t& params)
{
    checkCudaErrors(nvjpegDecoderCreate(params.nvjpeg_handle, NVJPEG_BACKEND_DEFAULT, &params.nvjpeg_decoder));
    checkCudaErrors(nvjpegDecoderStateCreate(params.nvjpeg_handle, params.nvjpeg_decoder, &params.nvjpeg_decoupled_state));

    checkCudaErrors(nvjpegBufferPinnedCreate(params.nvjpeg_handle, NULL, &params.pinned_buffers[0]));
    checkCudaErrors(nvjpegBufferPinnedCreate(params.nvjpeg_handle, NULL, &params.pinned_buffers[1]));
    checkCudaErrors(nvjpegBufferDeviceCreate(params.nvjpeg_handle, NULL, &params.device_buffer));

    checkCudaErrors(nvjpegJpegStreamCreate(params.nvjpeg_handle, &params.jpeg_streams[0]));
    checkCudaErrors(nvjpegJpegStreamCreate(params.nvjpeg_handle, &params.jpeg_streams[1]));

    checkCudaErrors(nvjpegDecodeParamsCreate(params.nvjpeg_handle, &params.nvjpeg_decode_params));
}

void destroy_decoupled_api_handles(decode_params_t& params)
{
    checkCudaErrors(nvjpegDecodeParamsDestroy(params.nvjpeg_decode_params));
    checkCudaErrors(nvjpegJpegStreamDestroy(params.jpeg_streams[0]));
    checkCudaErrors(nvjpegJpegStreamDestroy(params.jpeg_streams[1]));
    checkCudaErrors(nvjpegBufferPinnedDestroy(params.pinned_buffers[0]));
    checkCudaErrors(nvjpegBufferPinnedDestroy(params.pinned_buffers[1]));
    checkCudaErrors(nvjpegBufferDeviceDestroy(params.device_buffer));
    checkCudaErrors(nvjpegJpegStateDestroy(params.nvjpeg_decoupled_state));
    checkCudaErrors(nvjpegDecoderDestroy(params.nvjpeg_decoder));
}

void release_buffers(std::vector<nvjpegImage_t>& ibuf)
{
    for (int i = 0; i < ibuf.size(); i++)
    {
        for (int c = 0; c < NVJPEG_MAX_COMPONENT; c++)
        {
            if (ibuf[i].channel[c])
            {
                checkCudaErrors(cudaFree(ibuf[i].channel[c]));
            }
        }
    }
}

int decode_images(const FileData& img_data, const std::vector<size_t>& img_len, std::vector<nvjpegImage_t>& out, decode_params_t& params, double& time)
{
    checkCudaErrors(cudaStreamSynchronize(params.stream));
    cudaEvent_t startEvent = NULL, stopEvent = NULL;
    float loopTime = 0;

    checkCudaErrors(cudaEventCreate(&startEvent, cudaEventBlockingSync));
    checkCudaErrors(cudaEventCreate(&stopEvent, cudaEventBlockingSync));

    if (!params.batched)
    {
        printf("batched = false\n");
        if (!params.pipelined)  // decode one image at a time
        {
            checkCudaErrors(cudaEventRecord(startEvent, params.stream));
            for (int i = 0; i < params.batch_size; i++)
            {
                checkCudaErrors(nvjpegDecode(params.nvjpeg_handle, params.nvjpeg_state, (const unsigned char*)img_data[i].data(), img_len[i], params.fmt, &out[i], params.stream));
            }
            checkCudaErrors(cudaEventRecord(stopEvent, params.stream));
        }
        else
        {
            // use de-coupled API in pipelined mode
            checkCudaErrors(cudaEventRecord(startEvent, params.stream));
            checkCudaErrors(nvjpegStateAttachDeviceBuffer(params.nvjpeg_decoupled_state, params.device_buffer));
            int buffer_index = 0;
            checkCudaErrors(nvjpegDecodeParamsSetOutputFormat(params.nvjpeg_decode_params, params.fmt));
            for (int i = 0; i < params.batch_size; i++)
            {
                checkCudaErrors(nvjpegJpegStreamParse(params.nvjpeg_handle, (const unsigned char*)img_data[i].data(), img_len[i], 0, 0, params.jpeg_streams[buffer_index]));

                checkCudaErrors(nvjpegStateAttachPinnedBuffer(params.nvjpeg_decoupled_state, params.pinned_buffers[buffer_index]));

                checkCudaErrors(nvjpegDecodeJpegHost(params.nvjpeg_handle, params.nvjpeg_decoder, params.nvjpeg_decoupled_state, params.nvjpeg_decode_params, params.jpeg_streams[buffer_index]));

                checkCudaErrors(cudaStreamSynchronize(params.stream));

                checkCudaErrors(nvjpegDecodeJpegTransferToDevice(params.nvjpeg_handle, params.nvjpeg_decoder, params.nvjpeg_decoupled_state, params.jpeg_streams[buffer_index], params.stream));

                buffer_index = 1 - buffer_index; // switch pinned buffer in pipeline mode to avoid an extra sync

                checkCudaErrors(nvjpegDecodeJpegDevice(params.nvjpeg_handle, params.nvjpeg_decoder, params.nvjpeg_decoupled_state, &out[i], params.stream));
            }
            checkCudaErrors(cudaEventRecord(stopEvent, params.stream));
        }
    }
    else
    {
        printf("XXXXXXXXXXXXXXXX  batched = true\n");
        std::vector<const unsigned char*> raw_inputs;
        for (int i = 0; i < params.batch_size; i++)
        {
            raw_inputs.push_back((const unsigned char*)img_data[i].data());
        }

        checkCudaErrors(cudaEventRecord(startEvent, params.stream));
        checkCudaErrors(nvjpegDecodeBatched(params.nvjpeg_handle, params.nvjpeg_state, raw_inputs.data(), img_len.data(), out.data(), params.stream));
        checkCudaErrors(cudaEventRecord(stopEvent, params.stream));
    }
    checkCudaErrors(cudaEventSynchronize(stopEvent));
    checkCudaErrors(cudaEventElapsedTime(&loopTime, startEvent, stopEvent));
    time = static_cast<double>(loopTime);

    return EXIT_SUCCESS;
}

int write_images(std::vector<nvjpegImage_t>& iout, std::vector<int>& widths, std::vector<int>& heights, decode_params_t& params, FileNames& filenames)
{
    printf("\n�g�J�ɮ�, count = %d\n", params.batch_size);

    for (int i = 0; i < params.batch_size; i++)
    {
        // Get the file name, without extension.
        // This will be used to rename the output file.
        size_t position = filenames[i].rfind("/");
        std::string sFileName =
            (std::string::npos == position)
            ? filenames[i]
            : filenames[i].substr(position + 1, filenames[i].size());

        position = sFileName.rfind(".");

        sFileName = (std::string::npos == position) ? sFileName : sFileName.substr(0, position);

        //std::string fname(params.output_dir + "/" + sFileName + ".bmp");

        std::string fname("./" + sFileName + ".bmp");

        std::cout << "�ͦ��ɮ� : " << "    ./" + sFileName + ".bmp" << std::endl;

        int err;
        if (params.fmt == NVJPEG_OUTPUT_RGB || params.fmt == NVJPEG_OUTPUT_BGR)
        {
            //here
            err = writeBMP(fname.c_str(), iout[i].channel[0], iout[i].pitch[0],
                iout[i].channel[1], iout[i].pitch[1], iout[i].channel[2],
                iout[i].pitch[2], widths[i], heights[i]);
        }
        else if (params.fmt == NVJPEG_OUTPUT_RGBI || params.fmt == NVJPEG_OUTPUT_BGRI)
        {
            printf("XXXXXX case 2\n");
            // Write BMP from interleaved data
            err = writeBMPi(fname.c_str(), iout[i].channel[0], iout[i].pitch[0], widths[i], heights[i]);
        }

        if (err)
        {
            std::cout << "Cannot write output file: " << fname << std::endl;
            return EXIT_FAILURE;
        }
        std::cout << "Done writing decoded image to file: " << fname << ", " << widths[i] << " X " << heights[i] << std::endl;
    }
}

double process_images(FileNames& image_names, decode_params_t& params, double& total)
{
    // vector for storing raw files and file lengths
    FileData file_data(params.batch_size);
    std::vector<size_t> file_len(params.batch_size);
    FileNames current_names(params.batch_size);
    std::vector<int> widths(params.batch_size);
    std::vector<int> heights(params.batch_size);
    // we wrap over image files to process total_images of files
    FileNames::iterator file_iter = image_names.begin();

    std::cout << "process_images\n��Ƨ� : " << params.input_dir << "\n�ɮ׭Ӽ� : " << params.total_images << std::endl;
    std::cout << "batch_size : " << params.batch_size << std::endl;

    // stream for decoding
    checkCudaErrors(cudaStreamCreateWithFlags(&params.stream, cudaStreamNonBlocking));

    int total_processed = 0;

    // output buffers
    std::vector<nvjpegImage_t> iout(params.batch_size);
    // output buffer sizes, for convenience
    std::vector<nvjpegImage_t> isz(params.batch_size);

    for (int i = 0; i < iout.size(); i++)
    {
        for (int c = 0; c < NVJPEG_MAX_COMPONENT; c++)
        {
            iout[i].channel[c] = NULL;
            iout[i].pitch[c] = 0;
            isz[i].pitch[c] = 0;
        }
    }

    double test_time = 0;
    int warmup = 0;
    int total_numbers = 0;

    printf("\n�@�� %d ���ɮ�\n", params.total_images);

    while (total_processed < params.total_images)
    {
        total_numbers++;
        printf("\n�� %d ���ɮ�\n", total_numbers);

        if (read_next_batch(image_names, params.batch_size, file_iter, file_data, file_len, current_names))
        {
            return EXIT_FAILURE;
        }

        std::cout << "call prepare_buffers, filename = " << current_names[0] << std::endl;
        if (prepare_buffers(file_data, file_len, widths, heights, iout, isz, current_names, params))
        {
            return EXIT_FAILURE;
        }

        double time;
        if (decode_images(file_data, file_len, iout, params, time))
        {
            return EXIT_FAILURE;
        }
        if (warmup < params.warmup)
        {
            warmup++;
        }
        else
        {
            total_processed += params.batch_size;
            test_time += time;
        }

        std::cout << "�g�J�ɮ� W = " << widths[0] << ", H = " << heights[0] << ", name : " << current_names[0] << std::endl;
        write_images(iout, widths, heights, params, current_names);
    }
    total = test_time;

    release_buffers(iout);

    checkCudaErrors(cudaStreamDestroy(params.stream));

    return EXIT_SUCCESS;
}

// parse parameters
int findParamIndex(const char** argv, int argc, const char* parm)
{
    int count = 0;
    int index = -1;

    for (int i = 0; i < argc; i++)
    {
        if (strncmp(argv[i], parm, 100) == 0)
        {
            index = i;
            count++;
        }
    }

    if (count == 0 || count == 1)
    {
        return index;
    }
    else
    {
        std::cout << "Error, parameter " << parm
            << " has been specified more than once, exiting\n"
            << std::endl;
        return -1;
    }

    return -1;
}

int main(int argc, const char* argv[])
{
    std::cout << "main program" << std::endl;

    decode_params_t params;

    params.input_dir = "./images/";     //Ū�����ɪ���Ƨ���m
    params.batch_size = 1;
    params.total_images = -1;

    params.dev = 0;
    params.dev = findCudaDevice(argc, argv);

    params.warmup = 0;

    params.batched = false;
    params.pipelined = false;

    params.fmt = NVJPEG_OUTPUT_RGB; //�s�ɮ榡�ثe�u���RGB..  �YBMP

    params.write_decoded = false;

    cudaDeviceProp props;
    checkCudaErrors(cudaGetDeviceProperties(&props, params.dev));

    printf("Using GPU %d (%s, %d SMs, %d th/SM max, CC %d.%d, ECC %s)\n", params.dev, props.name, props.multiProcessorCount, props.maxThreadsPerMultiProcessor, props.major, props.minor, props.ECCEnabled ? "on" : "off");

    nvjpegDevAllocator_t dev_allocator = { &dev_malloc, &dev_free };
    nvjpegPinnedAllocator_t pinned_allocator = { &host_malloc, &host_free };
    int flags = 0;
    checkCudaErrors(nvjpegCreateEx(NVJPEG_BACKEND_DEFAULT, &dev_allocator, &pinned_allocator, flags, &params.nvjpeg_handle));

    checkCudaErrors(nvjpegJpegStateCreate(params.nvjpeg_handle, &params.nvjpeg_state));
    checkCudaErrors(nvjpegDecodeBatchedInitialize(params.nvjpeg_handle, params.nvjpeg_state, params.batch_size, 1, params.fmt));

    // read source images
    FileNames image_names;

    std::cout << "��Ƨ� : " << params.input_dir << std::endl;

    readInput(params.input_dir, image_names);
    params.total_images = image_names.size();

    std::cout << "�ɮ׭Ӽ� : " << image_names.size() << std::endl;
    std::cout << "�ɮ׭Ӽ� : " << params.total_images << std::endl;

    //printf("input_dir =  %s\n", params.input_dir); fail?
    printf("batch_size =  %d\n", params.batch_size);

    std::cout << "��Ƨ� : " << params.input_dir << "\n�ɮ׭Ӽ� : " << params.total_images << std::endl;
    std::cout << "batch_size : " << params.batch_size << std::endl;

    double total;

    printf("�}�l�B�z��Ƨ������Ҧ�����\n");
    if (process_images(image_names, params, total))
    {
        return EXIT_FAILURE;
    }

    std::cout << "\ntotal : " << total << " sec" << std::endl;
    std::cout << "Total decoding time: " << total << " sec" << std::endl;
    std::cout << "Avg decoding time per image: " << total / params.total_images << std::endl;
    std::cout << "Avg images per sec: " << params.total_images / total << std::endl;
    std::cout << "Avg decoding time per batch: " << total / ((params.total_images + params.batch_size - 1) / params.batch_size) << std::endl << std::endl;

    if (params.pipelined)
    {
        destroy_decoupled_api_handles(params);
    }

    checkCudaErrors(nvjpegJpegStateDestroy(params.nvjpeg_state));
    checkCudaErrors(nvjpegDestroy(params.nvjpeg_handle));

    return EXIT_SUCCESS;
}
