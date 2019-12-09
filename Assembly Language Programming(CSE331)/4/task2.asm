.model small
.stack 100h


.data 
        array db 1,2,3,4,5,"$"
        target db 3
        another_target db 8
        found_value db " Value Found$"
        not_found db "Value not Found$"

.code

    main proc
         
         mov ax,@data
         mov ds,ax
         
         loop:
            mov al,array[si]
            cmp al,target[0]
            cmp al,another_target[0]
        
            jz found
            cmp al,"$"
            jz notFound
            inc si
            jmp loop

            
            
        found:
            mov si,0
            foundLoop:
                mov al,found_value[si]
                cmp al,"$"
                jz end
                inc si
                mov dl,al
                mov ah,02h
                int 21h
                jmp foundLoop
       
            
            
        notFound:
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
            Hlt    
        
         
        
        
        
        
    endp main
    end main