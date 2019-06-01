Its AES128 ECB from what we can see
So we need to find the crypto blob, 16 byte and a key 16 byte.
From the key visual of the challenge we can decipher smth like "THCUDA" ... we assume it is "WITHCUDA"

https://github.com/sebastien-riou/aes-brute-force

$ ./aes-brute-force FFFFFFFF_FFFFFFFF_00000000_00000000 00000000_00000000_57495448_43554441 89504E47_0D0A1A0A_0000000D_49484452 7131AD54_EF04DBA5_03300C0F_F7BD838E 0x41 0x5a 16
INFO: 16 concurrent threads supported in hardware.

Search parameters:
  n_threads:    16
  key_mask:     FFFFFFFF_FFFFFFFF_00000000_00000000
  key_in:       00000000_00000000_57495448_43554441
  plain:        89504E47_0D0A1A0A_0000000D_49484452
  cipher:       7131AD54_EF04DBA5_03300C0F_F7BD838E
  byte_min:     0x41
  byte_max:     0x5A

  jobs_key_mask:00FFFFFF_FFFFFFFF_00000000_00000000

Launching 64 bits search

Thread 0 claims to have found the key
  key found:    41455343_5241434B_57495448_43554441

Performances:
  76609705504 AES128 operations done in 758.196s
  9ns per AES128 operation
  101.04 million keys per second

--> Use key on binary = Password: AESCRACKWITHCUDA

Either now run the binary on a machine with a capable NVIDIA CUDA card or just decipher the crypto blob by hand.

he19-xzCc-xElf-qJ4H-jay8

