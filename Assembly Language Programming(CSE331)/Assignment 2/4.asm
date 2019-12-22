include "emu8086.inc"
.model small        
.stack 100h

.data
    inputArray db 15,3,2,2,1,6,12
    outputArray db 6 dup(?)
.code

main proc   
    mov ax,@data
    mov ds,ax    
	
    CALL SCAN_NUM ;CX contains range input
    
    ;initializaion   
    mov si,0
    mov bh,1
    mov di,0
    inc cl  
    mov ah,0
        
    l1: 
        cmp bh,cl
        jz mid           
        mov al,inputArray[si]
        cmp al,bh
        jz found         ;if found,then straight start with new search
        inc si
        cmp si,7
        jz notFound      ;if not found, then append
                         ;it into the outputArray
        jmp l1
                
    found:
        mov si,0
        inc bh
        jmp l1
        
    notFound:
        mov outputArray[di],bh
        inc di
        jmp l1                       
    
     mid:                ;this segment is to show the output
        mov outputArray[di],'$'       
        mov di,0
        
        CALL PTHIS
        db 13, 10, 'Missing values are : ', 0        
        l2:
            mov al,outputArray[di]            
            cmp al,'$'
            jz end           
            CALL PTHIS
            db ' ', 0             
            CALL PRINT_NUM
            inc di
            jmp l2 
            
     end:
        DEFINE_SCAN_NUM
        DEFINE_PRINT_NUM
        DEFINE_PRINT_NUM_UNS
        DEFINE_PTHIS       
        hlt
  
endp main 
end main