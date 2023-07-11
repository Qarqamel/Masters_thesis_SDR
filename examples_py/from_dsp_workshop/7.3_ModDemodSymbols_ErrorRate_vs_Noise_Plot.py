import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol
from auxiliary_lib import my_plot

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

plt.rcdefaults()
plt.rc('font', size=8)
plt.rc('axes', titlesize=8)
plt.rc('axes', labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)
plt.rc('font', family='Arial')

RES = 100

plt.figure(figsize = [6.4, 2.4], dpi=RES)

for symbol_nr in 2,4,8:
    t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
    Carrier = np.sin(t) 
    Ref     = Carrier
    
    noise_deviation_list = np.linspace(0,5,20)
    
    err_nr_list = []
    for noise_deviation in noise_deviation_list:
    
        # TRANSMISION-RECEPTION
        symbols_tx = np.random.randint(0,symbol_nr,TRANSMISIONS_NR)    
        symbols_rx = list()
        for symbol in symbols_tx:        
            # modulation
            ampl = symbol_to_ampl(symbol_nr, symbol)
            Tx = ampl*Carrier        
            # real channel
            Rx = Tx + np.random.normal(0, noise_deviation, TIME_VECTOR_SIZE)   
            # demodulation
            ampl = (np.dot(Rx,Ref)/TIME_VECTOR_SIZE)*2  
            symbol = ampl_to_symbol(symbol_nr, ampl)
            
            symbols_rx.append(symbol)
        
        # Error calculation   
        symbols_rx = np.array(symbols_rx) # list to numpy array
        err_nr_list.append(sum(symbols_rx != symbols_tx))
    
    plt.plot(noise_deviation_list, err_nr_list, 'p-', label = f'symbol nr = {symbol_nr}')

plt.axhline(y=300,color='red', label='max error rate')
plt.xlabel('noise deviation')
plt.ylabel('error nr')
plt.grid()
plt.legend()
plt.show()

