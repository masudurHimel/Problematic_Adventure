include "emu8086.inc"
.model small
.stack 100h


.data

.code 


main proc 
        
        mov ax,7500h
        mov ds,ax
        
        CALL SCAN_NUM
        
        
        mov al,cl 
        
        CALL SCAN_NUM
        DEFINE_SCAN_NUM
        
        mov bl,cl
        
        
        ;main equation part
        
        sub al,1
        mov cl,al
        
        mul cl
        
        push ax
        
        sub bl,1
        mov al,bl
        
        mul bl
        
        pop cx
        
        add ax,cx 
        
        mov word ptr ds:[0010h],ax
        
    
    
    
endp main 
end main