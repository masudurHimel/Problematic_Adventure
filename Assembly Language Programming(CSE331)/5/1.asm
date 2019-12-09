.model small 
.stack 100h


.data


.code


main proc 
    
mov ax,7500h
mov ds,ax    

mov bl,100
mov al,12

mul bl

mov bx,0010h

mov word ptr ds:[bx],ax   

endp main
end main