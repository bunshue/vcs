A=imread('annie19980405.jpg');
fprintf('Dim of A = %s\n', mat2str(size(A)));
subplot(221); imshow(A); title('Original');
subplot(222); imshow(A(:, :, 1)); title('Red');
subplot(223); imshow(A(:, :, 2)); title('Green');
subplot(224); imshow(A(:, :, 3)); title('Blue');
