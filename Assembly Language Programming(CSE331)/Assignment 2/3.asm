include 'emu8086.inc'
.model small
.stack 100h

.data
      input db "ab123 cd$"  ; alphabet = 4, digit = 3 
                            ; will not count space
.code

main proc 
        
        mov ax,@data
        mov ds,ax
        
        mov si,0 
        mov cx,0
        mov dx,0
        
        l1:
            mov al,input[si] 
            
            cmp al,'$'
            jz end
            
            inc si       
            
            cmp al,'A'
            ja alphabet    ;above 'A', there's no chance of having a digit
            jb digit       ;below 'A', there's no chance of having a alphabet
            
        
        alphabet:
            inc cx
            jmp l1
            
        digit:  
            cmp al,20h     ; for avoiding space 
            jz  l1
            inc dx
            jmp l1
                           ; for showing output
        end:
            mov ax,cx
            CALL PTHIS
            db 13, 10, 'Alphabet : ', 0
            CALL PRINT_NUM    
            
            mov ax,dx
            CALL PTHIS
            db 13, 10, 'Digit : ', 0
            CALL PRINT_NUM   
            
            DEFINE_PRINT_NUM
            DEFINE_PRINT_NUM_UNS
            DEFINE_PTHIS
            
            
            hlt        
        
    
endp main
end main