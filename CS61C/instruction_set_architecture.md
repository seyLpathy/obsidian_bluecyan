# introduction to RISV
>[!definition]
>the language of the computer hardwares are  called ==instruction set==
# operatiosn on the computer
## hardware
the number of objects being operated by instruction set is fixed 
>the register size in risc-v architecture is 64bits. aka ox4.**doubleword**

**opname destination_register (source register1 register2)**
## 32 registers
convention marked as x0 to x31
x0 register is hard-wired to value zero
## data transfer instruction
A command that moves data between memory and registers
ld means load doubleword
>In many architectures, words must start at addresses that are multiples of 4 and doublewords must start at addresses that are multiples of 8. This requirement is called an alignment restriction

the offset is **byte addressing**
8bits 
 