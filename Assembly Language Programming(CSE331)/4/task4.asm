.model small
.stack 100h


.data 
    string1 db "FirstString$"
    string2 db "FjrstString$" 
    
    found_flag db "Same$"
    not_found db "Not same$"




.code

    main proc 
           
         mov ax,@data
         mov ds,ax   
            
         mov si,0
         
         loop:
            mov al,string1[si]
            mov ah,string2[si]
            
            inc si
            
            cmp al,"$"
            jz yes
            
            cmp al,ah
            jz loop
            
            jg greater
            
            jl lesser
           
            
            
              
        yes:
            mov si,0 
            mov bl,1
            foundLoop:
                mov al,found_flag[si]
                cmp al,"$"
                jz end
                inc si
                mov dl,al
                mov ah,02h
                int 21h
                jmp foundLoop
             
            
            
        greater:
            mov si,0 
            mov bl,1
            gfoundLoop:
                mov al,string1[si]
                cmp al,"$"
                jz end
                inc si
                mov dl,al
                mov ah,02h
                int 21h
                jmp gfoundLoop

            
        
        
        lesser:
            mov si,0 
            mov bl,1
            lfoundLoop:
                mov al,string2[si]
                cmp al,"$"
                jz end
                inc si
                mov dl,al
                mov ah,02h
                int 21h
                jmp lfoundLoop

               
    
        
        
        ;
;        no:
;            mov si,0
;            not_foundLoop:
;                mov al,not_found[si]
;                cmp al,"$"
;                jz end
;                inc si
;                mov dl,al
;                mov ah,02h
;                int 21h
;                jmp not_foundLoop
;                
;                
        end:
            hlt              
      
        
        
    endp main
    end main