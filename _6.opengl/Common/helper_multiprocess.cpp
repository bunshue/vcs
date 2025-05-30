#include "helper_multiprocess.h"
#include <cstdlib>
#include <string>

int sharedMemoryCreate(const char *name, size_t sz, sharedMemoryInfo *info) {
#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
  info->size = sz;
  info->shmHandle = CreateFileMapping(INVALID_HANDLE_VALUE, NULL,
                                      PAGE_READWRITE, 0, (DWORD)sz, name);
  if (info->shmHandle == 0) {
    return GetLastError();
  }

  info->addr = MapViewOfFile(info->shmHandle, FILE_MAP_ALL_ACCESS, 0, 0, sz);
  if (info->addr == NULL) {
    return GetLastError();
  }

  return 0;
#else
  int status = 0;

  info->size = sz;

  info->shmFd = shm_open(name, O_RDWR | O_CREAT, 0777);
  if (info->shmFd < 0) {
    return errno;
  }

  status = ftruncate(info->shmFd, sz);
  if (status != 0) {
    return status;
  }

  info->addr = mmap(0, sz, PROT_READ | PROT_WRITE, MAP_SHARED, info->shmFd, 0);
  if (info->addr == NULL) {
    return errno;
  }

  return 0;
#endif
}

int sharedMemoryOpen(const char *name, size_t sz, sharedMemoryInfo *info) {
#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
  info->size = sz;

  info->shmHandle = OpenFileMapping(FILE_MAP_ALL_ACCESS, FALSE, name);
  if (info->shmHandle == 0) {
    return GetLastError();
  }

  info->addr = MapViewOfFile(info->shmHandle, FILE_MAP_ALL_ACCESS, 0, 0, sz);
  if (info->addr == NULL) {
    return GetLastError();
  }

  return 0;
#else
  info->size = sz;

  info->shmFd = shm_open(name, O_RDWR, 0777);
  if (info->shmFd < 0) {
    return errno;
  }

  info->addr = mmap(0, sz, PROT_READ | PROT_WRITE, MAP_SHARED, info->shmFd, 0);
  if (info->addr == NULL) {
    return errno;
  }

  return 0;
#endif
}

void sharedMemoryClose(sharedMemoryInfo *info) {
#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
  if (info->addr) {
    UnmapViewOfFile(info->addr);
  }
  if (info->shmHandle) {
    CloseHandle(info->shmHandle);
  }
#else
  if (info->addr) {
    munmap(info->addr, info->size);
  }
  if (info->shmFd) {
    close(info->shmFd);
  }
#endif
}

int spawnProcess(Process *process, const char *app, char *const *args) {
#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
  STARTUPINFO si = {0};
  BOOL status;
  size_t arglen = 0;
  size_t argIdx = 0;
  std::string arg_string;
  memset(process, 0, sizeof(*process));

  while (*args) {
    arg_string.append(*args).append(1, ' ');
    args++;
  }

  status = CreateProcess(app, LPSTR(arg_string.c_str()), NULL, NULL, FALSE, 0,
                         NULL, NULL, &si, process);

  return status ? 0 : GetLastError();
#else
  *process = fork();
  if (*process == 0) {
    if (0 > execvp(app, args)) {
      return errno;
    }
  } else if (*process < 0) {
    return errno;
  }
  return 0;
#endif
}

int waitProcess(Process *process) {
#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
  DWORD exitCode;
  WaitForSingleObject(process->hProcess, INFINITE);
  GetExitCodeProcess(process->hProcess, &exitCode);
  CloseHandle(process->hProcess);
  CloseHandle(process->hThread);
  return (int)exitCode;
#else
  int status = 0;
  do {
    if (0 > waitpid(*process, &status, 0)) {
      return errno;
    }
  } while (!WIFEXITED(status));
  return WEXITSTATUS(status);
#endif
}

#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
// Generic name to build individual Mailslot names by appending process ids.
LPTSTR SlotName = (LPTSTR)TEXT("\\\\.\\mailslot\\sample_mailslot_");

int ipcCreateSocket(ipcHandle *&handle, const char *name,
                    const std::vector<Process> &processes) {
  handle = new ipcHandle;
  handle->hMailslot.resize(processes.size());

  // Open Mailslots of all clients and store respective handles.
  for (int i = 0; i < handle->hMailslot.size(); ++i) {
    std::basic_string<TCHAR> childSlotName(SlotName);
    char tempBuf[20];
    _itoa_s(processes[i].dwProcessId, tempBuf, 10);
    childSlotName += TEXT(tempBuf);

    HANDLE hFile =
        CreateFile(TEXT(childSlotName.c_str()), GENERIC_WRITE, FILE_SHARE_READ,
                   (LPSECURITY_ATTRIBUTES)NULL, OPEN_EXISTING,
                   FILE_ATTRIBUTE_NORMAL, (HANDLE)NULL);
    if (hFile == INVALID_HANDLE_VALUE) {
      printf("IPC failure: Opening Mailslot by CreateFile failed with %d\n",
             GetLastError());
      return -1;
    }
    handle->hMailslot[i] = hFile;
  }
  return 0;
}

int ipcOpenSocket(ipcHandle *&handle) {
  handle = new ipcHandle;
  HANDLE hSlot;

  std::basic_string<TCHAR> clientSlotName(SlotName);
  char tempBuf[20];
  _itoa_s(GetCurrentProcessId(), tempBuf, 10);
  clientSlotName += TEXT(tempBuf);

  hSlot = CreateMailslot((LPSTR)clientSlotName.c_str(), 0,
                         MAILSLOT_WAIT_FOREVER, (LPSECURITY_ATTRIBUTES)NULL);
  if (hSlot == INVALID_HANDLE_VALUE) {
    printf("IPC failure: CreateMailslot failed for client with %d\n",
           GetLastError());
    return -1;
  }

  handle->hMailslot.push_back(hSlot);
  return 0;
}

int ipcSendData(HANDLE mailslot, const void *data, size_t sz) {
  BOOL result;
  DWORD cbWritten;

  result = WriteFile(mailslot, data, (DWORD)sz, &cbWritten, (LPOVERLAPPED)NULL);
  if (!result) {
    printf("IPC failure: WriteFile failed with %d.\n", GetLastError());
    return -1;
  }
  return 0;
}

int ipcRecvData(ipcHandle *handle, void *data, size_t sz) {
  DWORD cbRead = 0;

  if (!ReadFile(handle->hMailslot[0], data, (DWORD)sz, &cbRead, NULL)) {
    printf("IPC failure: ReadFile failed with %d.\n", GetLastError());
    return -1;
  }

  if (sz != (size_t)cbRead) {
    printf(
        "IPC failure: ReadFile didn't receive the expected number of bytes\n");
    return -1;
  }

  return 0;
}

int ipcSendShareableHandles(
    ipcHandle *handle, const std::vector<ShareableHandle> &shareableHandles,
    const std::vector<Process> &processes) {
  // Send all shareable handles to every single process.
  for (int i = 0; i < processes.size(); i++) {
    HANDLE hProcess =
        OpenProcess(PROCESS_DUP_HANDLE, FALSE, processes[i].dwProcessId);
    if (hProcess == INVALID_HANDLE_VALUE) {
      printf("IPC failure: OpenProcess failed (%d)\n", GetLastError());
      return -1;
    }

    for (int j = 0; j < shareableHandles.size(); j++) {
      HANDLE hDup = INVALID_HANDLE_VALUE;
      // Duplicate the handle into the target process's space
      if (!DuplicateHandle(GetCurrentProcess(), shareableHandles[j], hProcess,
                           &hDup, 0, FALSE, DUPLICATE_SAME_ACCESS)) {
        printf("IPC failure: DuplicateHandle failed (%d)\n", GetLastError());
        return -1;
      }
      checkIpcErrors(ipcSendData(handle->hMailslot[i], &hDup, sizeof(hDup)));
    }
    CloseHandle(hProcess);
  }
  return 0;
}

int ipcRecvShareableHandles(ipcHandle *handle,
                            std::vector<ShareableHandle> &shareableHandles) {
  for (int i = 0; i < shareableHandles.size(); i++) {
    checkIpcErrors(
        ipcRecvData(handle, &shareableHandles[i], sizeof(shareableHandles[i])));
  }
  return 0;
}

int ipcCloseSocket(ipcHandle *handle) {
  for (int i = 0; i < handle->hMailslot.size(); i++) {
    CloseHandle(handle->hMailslot[i]);
  }
  delete handle;
  return 0;
}

int ipcCloseShareableHandle(ShareableHandle shHandle) {
  CloseHandle(shHandle);
  return 0;
}

#endif
