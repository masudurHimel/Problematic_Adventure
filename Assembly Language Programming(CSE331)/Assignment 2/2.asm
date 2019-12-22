include "emu8086.inc"
.model small
.stack 100h
.data      
    ;initializing 3*3 matrix      
    matrix db 1,2,3  ; row sum = 6  ;col sum = 12
           db 4,5,6  ; row sum = 15 ;col sum = 15 
           db 7,8,9  ; row sum = 24 ;col sum = 18
.code
main proc        
        mov ax,@data
        mov ds,ax  
		
        ;initialization
		
        mov ax,0
        mov si,0
        mov di,3
        
        row:
            mov bl,matrix[si]
            add al,bl           
            inc si
            cmp si,10
            jz mid
            cmp si,di
            jz result            
            jmp row
                      
        result:
            CALL PTHIS
            db 13, 10, 'Row Sum : ', 0
            CALL PRINT_NUM 
            mov ax,0
            add di,3
            jmp row  
                       
        ;column sum start from here               
        mid:
            mov ax,0
            mov si,0
            mov di,6
            mov cx,0
        
        col:
            mov bl,matrix[si]
            add al,bl           
            cmp si,8
            ja end
            cmp si,di
            jz colResult
            add si,3            
            jmp col
           
        colResult:
            CALL PTHIS
            db 13, 10, 'Column Sum : ', 0
            CALL PRINT_NUM  
            mov ax,0
            inc di 
            inc cx
            mov si,cx
            jmp col  
       
        DEFINE_PTHIS
        DEFINE_PRINT_NUM
        DEFINE_PRINT_NUM_UNS   
        
        end:
            hlt 
    
endp main
end main