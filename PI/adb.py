



class ADB
	def initialize
		@androidPath = "/sdcard/"
	end
	def push(fromfile, tofile=nil )
		if(tofile==nil)
			`adb push #{fromfile} #{@androidPath}#{fromfile}`
		end
	end
	def pull (fromfile, tofile=nil)
		if(tofile==nil)
			`adb pull #{@androidPath}#{fromfile}`
		end
	end
	def lstxt ()
		lsr = `adb shell ls -l /sdcard/*.txt`
		puts lsr
	end
	def ls (file)
		lsr = `adb shell ls -l #{@androidPath}#{file}`
		puts lsr
	end
	def rm (file)
		`adb shell rm #{@androidPath}#{file}`
	end
	def touch(file)
		`adb shell touch #{@androidPath}#{file}`
	end
	def timeStamp(file)
		tt = Time.now
		puts tt
		`echo #{tt} > #{file}` 
	end
end

if $0==__FILE__
	fn = "time.res"
	tt = Time.now
	puts tt

	`echo #{tt} > #{fn}` 
	#`adb push time.res /sdcard/frompi.txt`
	#`adb pull /sdcard/frompi.txt`
	adb = ADB.new
	adb.push(fn)
	sleep(2)
	tt = Time.now
	`echo #{tt} > #{fn}`
	puts tt
	
	adb.pull(fn)
	adb.ls(fn)
	adb.rm(fn)
	adb.ls(fn)
	adb.touch(fn)
	adb.ls(fn)


#touch block file on android
5.times do |idx|
	active_f = "act_#{idx}.txt"
	block_f = "block_#{idx}.txt"
	adb.touch(block_f)
	#generate result
	adb.timeStamp(active_f)	
	#copy result to phone
	adb.push(active_f)
	adb.lstxt
	#remove block file
	adb.rm(block_f)
	
end
	

end
