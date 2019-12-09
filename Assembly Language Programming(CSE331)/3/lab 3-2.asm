.model small
.stack 100h

.data


.code

main proc
	
	mov al,2
	mov dl,3
	
	mul dl 		;multiply dl*al(al is default)
	add al,1
	
			
	div dl		;8 bit (AL = quotient | Ah = remainder)
				;16 bit (AX = quotient | DX = remainder)
					
	
endp main
end main
