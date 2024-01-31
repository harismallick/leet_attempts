## 190. Reverse Bits
'''
Reverse bits of a given 32 bits unsigned integer.

'''
# Difficulty: Easy
# Bit manipulation question. Flip the binary, convert to integer, return.

def reverseBits(n: int) -> int:
    # binary = "{:032b}".format(n)
    # new_bin = binary[::-1]
    # n = int(new_bin, 2)
    # return n
    # My solution faster in Python, but the below solution is the bit manipulation technique with O(log32)
    #  // operation 1 - >  qrstuvwxyzABCDEFabcdefghijklmnop  
    n = ((( n & 0b11111111111111110000000000000000 ) >> 16 )  | (( n & 0b00000000000000001111111111111111 ) << 16))
	   
	#    // operation 2 - >  yzABCDEFqrstuvwxijklmnopabcdefgh
    n = ((( n & 0b11111111000000001111111100000000 ) >> 8  )  | (( n & 0b00000000111111110000000011111111 ) << 8 ))
	   
	#    // operation 3 -> CDEFyzABuvwxqrstmnopijklefghabcd 
    n = ((( n & 0b11110000111100001111000011110000 ) >> 4  )  | (( n & 0b00001111000011110000111100001111 ) << 4 ))
	   
	#    // operation 4 -> EFCDAByzwxuvstqropmnklijghefcdab
    n = ((( n & 0b11001100110011001100110011001100 ) >> 2  )  | (( n & 0b00110011001100110011001100110011 ) << 2 ))
	   
	#    // operation 5 ->  FEDCBAzyxwvutsrqponmlkjihgfedcba
    n = ((( n & 0b10101010101010101010101010101010 ) >> 1  )  | (( n & 0b01010101010101010101010101010101 ) << 1 ))
        
    return n

if __name__ == '__main__':
    print(reverseBits(43261596))