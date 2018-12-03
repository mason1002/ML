# Outlier Detection

https://scikit-learn.org/stable/modules/outlier_detection.html


## numpy.r_

### https://docs.scipy.org/doc/numpy/reference/generated/numpy.r_.html
### row-wise merging
numpy.r_ = <numpy.lib.index_tricks.RClass object>
Translates slice objects to concatenation along the first axis.

This is a simple way to build up arrays quickly. There are two use cases.

If the index expression contains comma separated arrays, then stack them along their first axis.
If the index expression contains slice notation or scalars then create a 1-D array with a range indicated by the slice notation.

### Example
```
>>>V = array([1,2,3,4,5,6 ])
>>>Y = array([7,8,9,10,11,12])
>>>np.r_[V[0:2],Y[0],V[3],Y[1:3],V[4:],Y[4:]]
array([ 1,  2,  7,  4,  8,  9,  5,  6, 11, 12])
```


```
>>> np.r_[np.array([1,2,3]), 0, 0, np.array([4,5,6])]
array([1, 2, 3, 0, 0, 4, 5, 6])
>>> np.r_[-1:1:6j, [0]*3, 5, 6]
array([-1. , -0.6, -0.2,  0.2,  0.6,  1. ,  0. ,  0. ,  0. ,  5. ,  6. ])
```
String integers specify the axis to concatenate along or the minimum number of dimensions to force entries into.

```
>>> a = np.array([[0, 1, 2], [3, 4, 5]])
>>> np.r_['-1', a, a] # concatenate along last axis
array([[0, 1, 2, 0, 1, 2],
       [3, 4, 5, 3, 4, 5]])
>>> np.r_['0,2', [1,2,3], [4,5,6]] # concatenate along first axis, dim>=2
array([[1, 2, 3],
       [4, 5, 6]])
```
```
>>> np.r_['0,2,0', [1,2,3], [4,5,6]]
array([[1],
       [2],
       [3],
       [4],
       [5],
       [6]])
>>> np.r_['1,2,0', [1,2,3], [4,5,6]]
array([[1, 4],
       [2, 5],
       [3, 6]])
 ```
 Using ‘r’ or ‘c’ as a first string argument creates a matrix.
 ```
 >>> np.r_['r',[1,2,3], [4,5,6]]
matrix([[1, 2, 3, 4, 5, 6]])
```
## sklearn.covariance.EllipticEnvelope
https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html
- covariance:协方差
### How to apply sklearn's EllipticEnvelope to find out top outliers in the given dataset?
https://stackoverflow.com/questions/33778802/how-to-apply-sklearns-ellipticenvelope-to-find-out-top-outliers-in-the-given-da

# Reference
https://blog.csdn.net/scdxmoe/article/details/53741521
