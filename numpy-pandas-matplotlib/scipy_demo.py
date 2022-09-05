from scipy import io
import numpy as np

if __name__ == "__main__":
    arr = np.arange(10)
    io.savemat('scipydemo.mat', {"vec": arr})
    mydata = io.loadmat('scipydemo.mat',squeeze_me=True)
    print(mydata, type(mydata),mydata['vec'],type(mydata['vec']))
