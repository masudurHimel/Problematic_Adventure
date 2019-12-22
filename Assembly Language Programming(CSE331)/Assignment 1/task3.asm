.model small
.stack 100h


.data 

        targetArray db 9,8,7,1,2,3,0,4,5,6 ;randomly 0-9 taken as in ASCII 48-57 are 0-9 
        tempArray db ?
        minString db "Minimum: $"
        maxString db "   Maximum: $"
        

.code 




main proc 
    
        mov ax,@data
        mov ds,ax
        
        mov di,-1
        mov al,targetArray[0]        ;selecting the first value of array for further testing
             
        minLoop:
            inc di
            mov bl,targetArray[di]   ;selecting next value for testing
            cmp di,10
            jz min
            cmp bl,al
            jl minTemp               ;jumping to minTemp  for reorganizing the comparing values
            jmp minLoop        
                    
    
    
    
        minTemp:                     ;value of al is reset for further testing
           mov al,bl
           jmp minLoop
           
        
        min:
           mov tempArray[0],al
           mov si,0
           jmp minPrint
           
           
        minPrint:                     ;for printing "Minimum"
           
           mov ah,02
           mov dl,minString[si] 
           cmp dl,'$'
           jz minResult
           int 21h 
           inc si
           jmp minPrint
           
           
        minResult:                    ;for printing minimum value
           mov ah,02
           mov al,tempArray[0]
           add al,48
           mov dl,al
           int 21h
           jmp mid 
           
           
        mid:                          ;initialization for maximum part
            mov di,-1
            mov al,targetArray[0]
             
        maxLoop:                      ;same algorithm as the minimum one
            inc di
            mov bl,targetArray[di]
            cmp di,10
            jz max
            cmp bl,al
            jg maxTemp
            jmp maxLoop
            
            
            
        maxTemp:
           mov al,bl
           jmp maxLoop
           
        
        max:
           mov tempArray[0],al
           mov si,0
           jmp maxPrint
            
            
        maxPrint:                     ;for printing "Maximum"
           mov ah,02
           mov dl,maxString[si] 
           cmp dl,'$'
           jz maxResult
           int 21h 
           inc si
           jmp maxPrint
           
           
        maxResult:                    ;for printing maximum value
           mov ah,02
           mov al,tempArray[0]
           add al,48
           mov dl,al
           int 21h
           jmp end        
           
           
        end:
            hlt    
            
            
            
endp main
end main