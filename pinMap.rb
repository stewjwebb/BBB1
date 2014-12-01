
class Pin
	attr_accessor :headPin, :pin, :gpioNum, :mode
	def initialize(headPin, pin, gpioNum)
		@headPin = headPin
		@pin = pin
		@gpioNum = gpioNum
		@mode = nil
	end

	def self.map_mode(mode)
		#state = [0, 1, 2, 3, 4, 5, 6]
		#state = ["slewCtrl", "rxactive", "pullUpType", "notEnabled", "Mode"] 
		#state = ["mode", "pullNotEnabled", :pullUpType", "rxactive", "slewCtrl"]

		str = "#{mode} #{mode.class} #{mode & 7} "
		if((mode.to_i&7.to_i) == 7)
			str += "GPIO"
		else
			str += "UNKWN"
		end

		if(((mode>>3)&0x1) == 1)
			str += " pullNotEnabled"
		else 
			str += " pullIsEnabled"
		end
		
		puts "4..#{((mode>>4)&1)}"

		if(((mode>>4)&1) == 1)
			str += " pullUppp"
		else 
			str += " pullDown"
		end


		if(((mode>>5)&1)==1)
			str += " fastSlew"
		else
			str += " slowSlew"
		end
		
		puts str
	end

end


red = IO.readlines("/sys/kernel/debug/pinctrl/44e10800.pinmux/pins")



headPin = ["P9_11", "P9_12", "P9_13", "P9_14", "P9_15", "P9_16", "P9_17", "P9_18", "P9_27"] 
pin     = [28, 30, 29, 18, 16, 19, 87, 86, 105]
gpioNum = [40, 60, 31, 50, 48, 51,  5,  4, 115]
mode = []

puts headPin.size
puts pin.size
puts gpioNum.size

pins = []
idx = 0

headPin.size.times do |idx|
	puts "idx #{idx}"
	tpin = Pin.new(headPin[idx], pin[idx], gpioNum[idx])
	puts "after"
	pins << tpin
end
pins.each do |pp|
	p pp
end

red.each do |line|
	pin.each do |pp|
    	if(line =~ /pin #{pp} /)
	     sp = line.split
		 mode << sp[3].to_i(16)
		 #Pin.map_mode(sp[3].to_i(16))
    	 puts line
    	end
	end
end
p mode

mode.each do |md|
		puts "mode #{md}"
		 Pin.map_mode(md.to_i)

end

#Pin.map_mode(15)
#pins = Array.new
#
#headPin.size.times do |idx|
#
#	pin = Pin.new(headPin[idx], pin[idx], gpioNum[idx])
#	pins << pin
#end
#
#p pins
