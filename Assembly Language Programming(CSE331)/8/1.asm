include 'emu8086.inc'
.model small 
.stack 100h



.data
     input db ?
     output db 10 dup(?)
           db 10 dup(?)



.code 

iMatrix proc
    
    loop:
        mov al,cl
        mul si
        add ax,si  
        mov di,ax
        mov output[di],1
        
        inc si
        cmp si,cx
        jz end
        jmp loop
    
    
iMatrix endp    

main proc 
    
     mov ax,@data
     mov ds,ax
     
     CALL SCAN_NUM
     DEFINE_SCAN_NUM
     
     mov input,cl
     mov al,cl 
     mov ah,0
     mov dl,cl 
     
     mov ch,0
     mov si,0
     
     call iMatrix
        
        
        
    end:
        hlt     
        
     
     
     
    
    
    
endp main
end main

          

     