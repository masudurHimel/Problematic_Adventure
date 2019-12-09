.model small
.stack 100h


.data
        firstArray db 1,2,3,4,5
        secondArray db 5,4,3,2,1
        sumArray db ?

.code

main proc
    mov ax,@data
    mov ds,ax
    
    
    mov si,0
    
    l1:
        mov al,firstArray[si]
        mov bl,secondArray[si]
        
        add al,bl
        
        mov sumArray[si],al
        
        inc si
        cmp si,6
        jz end
        jmp l1
        
        
    end:
        hlt    
    
    
    
endp main
end main