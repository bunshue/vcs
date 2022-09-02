using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

using System.IO;
using System.Security.Cryptography;
using System.Diagnostics;

namespace howto_password_tracker
{
    public static class Crypto
    {
        // The random number provider.
        private static RNGCryptoServiceProvider Rand = new RNGCryptoServiceProvider();

#region Random Selection Methods

        // Return a random integer between a min and max value.
        public static int RandomInteger(int min, int max)
        {
            uint scale = uint.MaxValue;
            while (scale == uint.MaxValue)
            {
                // Get four random bytes.
                byte[] four_bytes = new byte[4];
                Rand.GetBytes(four_bytes);

                // Convert that into an uint.
                scale = BitConverter.ToUInt32(four_bytes, 0);
            }

            // Add min to the scaled difference between max and min.
            return (int)(min + (max - min) * (scale / (double)uint.MaxValue));
        }

#endregion Random Selection Methods

#region Encryption Methods

        // Encrypt a string into a hex byte string.
        public static string EncryptToString(string plain_text, string password, string salt)
        {
            return BytesToHexString(Encrypt(plain_text, password, salt));
        }

        // Decrypt a string from a hex byte string.
        public static string DecryptFromString(string encrypted_bytes_string, string password, string salt)
        {
            return Decrypt(HexStringToBytes(encrypted_bytes_string), password, salt);
        }

        // Encrypt a string into an array of bytes.
        private static byte[] Encrypt(string plain_text, string password, string salt)
        {
            ASCIIEncoding ascii_encoder = new ASCIIEncoding();
            byte[] plain_bytes = ascii_encoder.GetBytes(plain_text);
            return CryptBytes(password, plain_bytes, salt, true);
        }

        // Decrypt a string from an array of bytes.
        private static string Decrypt(byte[] encrypted_bytes, string password, string salt)
        {
            byte[] decrypted_bytes = CryptBytes(password, encrypted_bytes, salt, false);
            ASCIIEncoding ascii_encoder = new ASCIIEncoding();
            return new string(ascii_encoder.GetChars(decrypted_bytes));
        }

        // Convert bytes into a string.
        private static string BytesToHexString(byte[] bytes)
        {
            string result = "";
            foreach (byte b in bytes)
            {
                result += " " + b.ToString("X2");
            }
            if (result.Length > 0) result = result.Substring(1);
            return result;
        }

        // Convert a hex string into bytes.
        private static byte[] HexStringToBytes(string str)
        {
            str = str.Replace(" ", "");
            int num_bytes = str.Length / 2;
            byte[] bytes = new byte[num_bytes];
            for (int i = 0; i < num_bytes; i++)
            {
                bytes[i] = Convert.ToByte(str.Substring(2 * i, 2), 16);
            }
            return bytes;
        }

        // Use the password to generate key bytes.
        private static void MakeKeyAndIV(string password, byte[] salt, int key_size_bits, int block_size_bits, ref byte[] key, ref byte[] iv)
        {
            Rfc2898DeriveBytes derive_bytes = new Rfc2898DeriveBytes(password, salt, 513);
            key = derive_bytes.GetBytes(key_size_bits / 8);
            iv = derive_bytes.GetBytes(block_size_bits / 8);
        }

        // Encrypt or decrypt a byte array.
        private static byte[] CryptBytes(string password, byte[] in_bytes, string salt, bool encrypt)
        {
            // Make an AES service provider.
            AesCryptoServiceProvider aes_provider = new AesCryptoServiceProvider();

            // Find a valid key size for this provider.
            int key_size_bits = 0;
            for (int i = 1024; i >= 1; i--)
            {
                if (aes_provider.ValidKeySize(i))
                {
                    key_size_bits = i;
                    break;
                }
            }
            Debug.Assert(key_size_bits > 0);

            // Get the block size for this provider.
            int block_size_bits = aes_provider.BlockSize;

            // Convert the salt into bytes.
            byte[] salt_bytes = HexStringToBytes(salt);

            // Generate the key and initialization vector.
            byte[] key = null;
            byte[] iv = null;
            MakeKeyAndIV(password, salt_bytes, key_size_bits, block_size_bits, ref key, ref iv);

            // Make the encryptor or decryptor.
            ICryptoTransform crypto_transform;
            if (encrypt) crypto_transform = aes_provider.CreateEncryptor(key, iv);
            else crypto_transform = aes_provider.CreateDecryptor(key, iv);

            // Create the output stream.
            MemoryStream out_stream = new MemoryStream();

            // Attach a crypto stream to the output stream.
            CryptoStream crypto_stream = new CryptoStream(
               out_stream, crypto_transform,
               CryptoStreamMode.Write);

            // Write the bytes into the CryptoStream.
            crypto_stream.Write(in_bytes, 0, in_bytes.Length);
            try
            {
                crypto_stream.FlushFinalBlock();
            }
            catch (CryptographicException)
            {
                // Ignore this one. The password is bad.
            }
            catch
            {
                // Re-raise this one.
                throw;
            }

            // Save the result.
            byte[] result = out_stream.ToArray();

            // Close the stream.
            try
            {
                crypto_stream.Close();
            }
            catch (CryptographicException)
            {
                // Ignore this one. The password is bad.
            }
            catch
            {
                // Re-raise this one.
                throw;
            }
            out_stream.Close();

            return result;
        }

        // Return a pseudo-random salt.
        public static string RandomSalt()
        {
            // Pick a random number of bytes.
            int num_bytes = RandomInteger(10, 20);

            // Fill the salt array.
            byte[] salt_bytes = new byte[num_bytes];
            Rand.GetBytes(salt_bytes);

            // Return the salt converted into a hex string.
            return BytesToHexString(salt_bytes);
        }
       
#endregion Encryption Methods

    }
}
