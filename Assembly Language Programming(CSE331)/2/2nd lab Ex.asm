.model small
.stack 100h 



.data

  firstArray db 1,2,3,4,5
  secondArray db ?
                          

                          

.code


main proc   
    mov ax, @data
    mov ds,ax 
    
    mov al,firstArray[4]
    mov secondArray[0],al
    mov ah,secondArray[0] 
    
    mov al,firstArray[3]
    mov secondArray[1],al
    mov ah,secondArray[1]

    mov al,firstArray[2]
    mov secondArray[2],al
    mov ah,secondArray[2]
    
    mov al,firstArray[1]
    mov secondArray[3],al
    mov ah,secondArray[3]
    
    mov al,firstArray[0]
    mov secondArray[4],al
    mov ah,secondArray[4]

        

endp main
end main
