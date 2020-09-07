import visa

rm = visa.ResourceManager()
print(rm.list_resources())
my_instrument = rm.open_resource('GPIB0::17::INSTR')
print(my_instrument.query('*IDN?'))
print(my_instrument)


my_instrument.write('reset()')
my_instrument.write('smua.reset()')
my_instrument.write('smua.nvbuffer1.clear()')
my_instrument.write('smua.nvbuffer1.clearcache()')
my_instrument.write('smua.source.func=0')
my_instrument.write('smua.source.leveli=0.1')
my_instrument.write('smua.measure.delay=0.1')
my_instrument.write('smua.source.limitv=100')
my_instrument.write('smua.source.output=1')
my_instrument.write('smua.measure.v(smua.nvbuffer1)')
my_instrument.write('print(smua.nvbuffer1[1])')
my_instrument.write('smua.source.output=0')
my_instrument.write('reset()')


my_instrument = rm.close()
