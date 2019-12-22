include "emu8086.inc"
.model small
.stack 100h


.data
    

.code


main proc
        
        mov ax,@data
        mov ds,ax  
        
        ;initialization
        mov ax,0
        
        ;input al = AAh, output will be same
        
        mov al,0AAh  
                 
        mov bl,10h
        div bl
        
        cmp ah,al ;for comparing lower and higher nibble
        jz same
        jmp notSame 
        
        
        same:                
            CALL PTHIS
            db 13, 10, 'SAME',0        
            jmp end
                        
                        
        notSame:
            CALL PTHIS
            db 13, 10, 'NOT SAME',0
                    
        
        end:
            DEFINE_PTHIS
            hlt
                           
            
        
        
        
    
    
endp main
end main