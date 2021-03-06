.model small
.stack 100h

.data
    
    palindrome db "racecary$"
    non_palindrome db "hellyeah$"
   
    tempValue db ?  
    
    
    found_flag db "Yes ! Is is a Palindrome$"
    not_found db "Not a palindrome$"



.code

main proc
    
    mov ax,@data
    mov ds,ax
    
    
    mov si,0
    
    loop:
        mov al,palindrome[si]
        cmp al,"$"
        jz mid
        mov ah,0
        push ax
        inc si
        jmp loop
        
        
    mid:
        mov di,si
        mov si,0
        jmp tempLoop 
        
        
    tempLoop:
        cmp di,0
        jz resultMid
        pop ax
        mov tempValue[si],al
        dec di
        inc si
        jmp tempLoop
        
        
    resultMid:
        mov si,0
        
    result:
        mov al,palindrome[si]
        mov bl,tempValue[si]

        cmp al,"$"
        jz yes
        
        cmp al,bl
        jnz no
        
        inc si
        jmp result
        
        
        
    yes:
        mov si,0 
        mov bl,1
        mov cx,3
        foundLoop:
            mov al,found_flag[si]
            cmp al,"$"
            jz end
            inc si
            mov dl,al
            mov ah,02h
            int 21h
            loop foundLoop

        
        
        
    no:
        mov si,0
        not_foundLoop:
            mov al,not_found[si]
            cmp al,"$"
            jz end
            inc si
            mov dl,al
            mov ah,02h
            int 21h
            jmp not_foundLoop
            
            
    end:
        hlt                  
        
 
    
    
endp main
end main