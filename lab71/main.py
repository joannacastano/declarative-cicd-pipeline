def sender(A):
  # Assume that the parity bit is the last bit of the codeword
  n = len(A) + 1
  codeword = ""
  ones = 0

  # Calculate the parity bit
  parity = '0'
  for i in range(n - 1):
    if A[i] == 1:
      ones += 1

  if ones % 2 != 0:
    parity = '1'

  A = [str(j) for j in A]
  codeword = codeword.join(A)
  
  print("Codeword: ", codeword+parity)

  return 0
  
def receiver(data_word, codeword):
  # First, we check the length of the data word and codeword
  k = len(data_word)
  n = len(codeword)

  # If the length of the codeword is not equal to the length of the data word plus one,
  # then the codeword is invalid and we return "Discarded"
  if n != k + 1:
    return "Discarded"

  # Next, we calculate the parity of the codeword. This is done by summing the
  # values of all the bits in the codeword and taking the modulo 2.
  parity = sum(codeword) % 2

  # If the parity is 0, then the codeword is valid and we can extract the
  # original data word from it.
  if parity == 0:
    # To extract the data word, we simply remove the last bit from the codeword
    return ''.join(map(str, codeword[:-1]))
  else:
    # If the parity is not 0, then the codeword is invalid and we return "Discarded"
    return "Discarded"


# Test the sender and receiver
A = input("Input A: ")
A = [*A]
data_word = [int(i) for i in A]
sender(data_word)

B = input("Input B: ")
B = [*B]
codeword = [int(j) for j in B]

data = receiver(data_word, codeword)
print("Data word: ", data)