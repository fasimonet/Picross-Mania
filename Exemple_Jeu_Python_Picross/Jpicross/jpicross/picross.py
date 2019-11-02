from pygame import *
import jmenu
init()

font0=font.Font(font.get_default_font(),15)
font1=font.Font(font.get_default_font(),40)
font2=font.Font(font.get_default_font(),20)

screen=display.set_mode((900,900))

def play(choix):
	def ll(p):
		a=['0']+list(p)+['0']
		b=[a[:h].count('1')for h,i in enumerate(a)if not int(i)] 
		return [j-b[i]for i,j in enumerate(b[1:])if j-b[i]]
	global gx,choix2
	def mm(p0,p1):
		for p in p1:picross[0].append(ll(p))
		for p in p0:picross[1].append(ll(p))
		[screen.blit(font0.render(str(i).rjust(2),1,(25,25,25)),((y%gx)*21+265,(y/gx)*17+5))for y,i in enumerate(sum((zip(*[(15-len(i))*['']+i for i in picross[0]])),()))if i]
		[screen.blit(font0.render(str(i).rjust(2),1,(25,25,25)),((y%15)*17+2,(y/15)*21+268))for y,i in enumerate(sum([(15-len(i))*['']+i for i in picross[1]],[]))if i]
			
	time.set_timer(USEREVENT+1,0)
	choix2=None
	while True:
		mtr=None
		if choix==None:break
		if choix=='PLAY':
			screen.fill((200,200,200));screen.blit(goback,gbrect.topleft)
			try:
				f=jmenu.run([i.split(';')[0]for i in r],(128,128,128),30,(10,10,100),justify=True,pos=('center','top'))
				picross=eval(r[[i.split(';')[0]for i in r].index(f)].split(';')[1])
			except:event.clear();event.post(event.Event(USEREVENT+1));break
			while picross[0]==0:del(picross[0])
			while picross[-1]==0:del(picross[-1])
			gx,gy = len(bin(max(picross)))-2,len(picross)
			p0=[list(bin(x)[2:].zfill(gx))for x in picross]
			p1=zip(*p0)
			while not any(map(int,p1[-1])):del(p1[-1])
			p0=zip(*p1);gx=len(p1)
			picross=[[],[]]
			mm(p0,p1)
			time.set_timer(USEREVENT+1,1000)
		else:
			screen.fill((200,200,200));screen.blit(goback,gbrect.topleft);gx,gy=30,30
			if choix2!='EDIT':
				choix2=jmenu.run(['NEW','EDIT'],(128,128,128),30,(10,10,100))
			if choix2==None:event.clear();event.post(event.Event(USEREVENT+1));break
			if choix2=='EDIT':
				try:
					f=jmenu.run([i.split(';')[0]for i in r],(128,128,128),30,(10,10,100),justify=True,pos=('center','top'))
					picross=eval(r[[i.split(';')[0]for i in r].index(f)].split(';')[1])
				except:event.clear();break
				screen.blit(font2.render(f,1,(10,10,10)),(0,0))
				mtr=sum([list(bin(x)[2:].zfill(gx))for x in picross],[])+['0']*(901-len(picross))
				p0=[list(bin(x)[2:].zfill(gx))for x in picross]
				p1=zip(*p0)
				picross=[[],[]]
				mm(p0,p1)
			saverect=screen.blit(font1.render('SAVE',1,(128,128,128)),(0,20))
			
		screen.fill(0,(264,264,gx*21+1,gy*21+1))
		grid=[screen.fill((200,200,200),(265+(i%gx)*21,265+(i/gx)*21,20,20)) for i in range(gx*gy)]+[Rect((-20,-20,0,0))]
		if mtr:[screen.fill((100,100,100),grid[x])for x,y in enumerate(mtr)if int(y)]
		else:mtr=['0']*gx*gy+['0']
		prez=-1;out=[[[]]*gx,[[]]*gy];display.flip()
		event.set_allowed(None);event.set_allowed((MOUSEBUTTONDOWN,QUIT,USEREVENT+1,MOUSEMOTION,KEYDOWN))
		if choix=='PLAY':ticks=-1;event.post(event.Event(USEREVENT+1));screen.blit(font2.render(f+' : '+str(gx)+'x'+str(gy),1,(10,10,10)),(0,0))

		while True:
			e=event.wait()
			if e.type==QUIT or key.get_pressed()[K_ESCAPE]:break
			if e.type==USEREVENT+1:
				ticks+=1
				screen.fill((200,200,200),(0,20,264,244))
				screen.blit(font1.render(str(ticks/3600).zfill(2)+':'+str(ticks%3600/60).zfill(2)+':'+str(ticks%60).zfill(2),1,(128,128,128)),(0,20))
				display.flip()
				continue
			z=Rect(mouse.get_pos(),(1,1)).collidelist(grid)
			if e.type==MOUSEMOTION:
				if prez!=z and choix=='PLAY'and z>-1:
					screen.fill((200,200,200),(grid[prez].left,0,21,264));screen.fill((200,200,200),(0,grid[prez].top,264,21))
					[screen.blit(font0.render(str(i).rjust(2),1,(25,25,25)),((prez%gx)*21+265,y*17+5))for y,i in enumerate((15-len(picross[0][prez%gx]))*['']+picross[0][prez%gx])if i]
					[screen.blit(font0.render(str(i).rjust(2),1,(25,25,25)),(y*17+2,(prez/gx)*21+268))for y,i in enumerate((15-len(picross[1][prez/gx]))*['']+picross[1][prez/gx])if i]
					prez=z
					w=(15-len(picross[0][prez%gx]));screen.fill((255,255,255),(grid[prez].left,w*17,21,264-w*17))
					[screen.blit(font0.render(str(i).rjust(2),1,(100,10,10)),((prez%gx)*21+265,y*17+5))for y,i in enumerate(w*['']+picross[0][prez%gx])if i]
					w=(15-len(picross[1][prez/gx]));screen.fill((255,255,255),(w*17,grid[prez].top,264-w*17,21))
					[screen.blit(font0.render(str(i).rjust(2),1,(100,10,10)),(y*17+2,(prez/gx)*21+268))for y,i in enumerate(w*['']+picross[1][prez/gx])if i]
					display.flip()
				continue
			if z>-1 and e.type==MOUSEBUTTONDOWN:
				if e.button==1:
					screen.fill((200,200,200)if mtr[z]=='1' else (100,100,100),grid[z]);mtr[z]='1'if mtr[z]=='0' else'0'
					out[0][z%gx]=ll(mtr[z%gx::gx])
					out[1][z/gx]=ll(mtr[(z/gx)*gx:(z/gx+1)*gx])
					if choix=='PLAY' and out==picross:
						if [tuple(mtr[x:x+gx])for x in range(0,gx*gy,gx)]==p0:
							screen.blit(font1.render('YOU WIN',1,(75,75,75)),(0,60))
							screen.blit(font0.render('press button to continue',1,(0,0,0)),(0,100))

							[screen.fill((0,0,0),grid[x])for x,y in enumerate(mtr)if int(y)]
							#[draw.circle(screen, (0,0,0), grid[x].center, 15, 0)for x,y in enumerate(mtr)if int(y)]
							display.flip()
							while event.wait().type != MOUSEBUTTONDOWN:pass
							break
						else:
							screen.blit(font1.render('ALMOST',1,(75,75,75)),(0,60))
							display.flip()
							while event.wait().type != MOUSEMOTION:pass
					elif choix=='MAKE or EDIT GRID':
						screen.fill((200,200,200),(grid[z].left,0,21,264));screen.fill((200,200,200),(0,grid[z].top,264,21))
						[screen.blit(font0.render(str(i).rjust(2),1,(25,25,25)),((z%30)*21+265,y*17+5))for y,i in enumerate((15-len(out[0][z%gx]))*['']+out[0][z%gx])if i]
						[screen.blit(font0.render(str(i).rjust(2),1,(25,25,25)),(y*17+2,(z/30)*21+268))for y,i in enumerate((15-len(out[1][z/gx]))*['']+out[1][z/gx])if i]
				elif e.button==3 and choix=='PLAY':
					screen.fill(screen.get_at(grid[z].topleft)if screen.get_at(grid[z].center)==(200,100,100)else(200,100,100),grid[z].inflate(-21/2,-21/2))
			elif choix=='MAKE or EDIT GRID':
						if saverect.collidepoint(mouse.get_pos()):
							out=[int(''.join(y),2)for y in[mtr[x:x+gx] for x in range(0,900,30)]]
							with open('picross2.txt','w') as p:p.write(''.join(r)+str(len(r))+';'+str(out)+'\n')
							break
			display.flip()
		[event.set_allowed(e) for e in range(0,31)]

goback=font0.render('HIT ESCAPE OR KILL WINDOW TO GO BACK',1,(50,50,50))
gbrect=goback.get_rect();gbrect.center=(450,850)
pimg=image.load('picross.png')
while event.wait().type != QUIT:
	screen.fill((200,200,200))
	screen.blit(pimg,(40,0))
	screen.blit(goback,gbrect.topleft)
	try:
		with open('picross2.txt','r') as r:r=r.readlines()
	except:r=[]
	play(jmenu.run(['PLAY','MAKE or EDIT GRID']if r else['MAKE or EDIT GRID'],(128,128,128),30,(10,10,100)))
	while choix2=='EDIT':play('MAKE or EDIT GRID')
