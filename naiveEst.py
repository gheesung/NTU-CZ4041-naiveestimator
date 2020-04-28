# Submitted by Ng Ghee Sung
# K1920070J

def readfile():
  f = open(fname, "r")
  count=0
  arr =[]
  for line in f:
    if count == 0:  # Extract the Header
      dim=line.split(",")
      dim=[float(i) for i in dim]
    if count >0:    # Extract the dataset
      val=line.split(" ")
      val=[float(i) for i in val]
      arr.append(val)
    count +=1
  return dim, arr

def WindowFunction(a,b):
  # compute Euclidean distance between the point
  dist = sum([(a1 - b1) ** 2 for a1, b1 in zip(a, b)])**(0.5)
  #print ("Euclidean dist ", a, " and ", b, "is :", dist)
  if dist/bw < 0.5 :
    return 1
  return 0

def NaiveEstimator(x) :
  count = 0
  for row in X :
    count += WindowFunction(x, row)
  return count/(n*V), count

print("\n\nNaive Estimator - Non-Parametric Density Estimation\n")
fname ='data.txt'      # input filename
ofname ='output.txt'   # output filename
dim, X = readfile()   # get the dim and the dataset from the file
bw = 2                # the bin width
n = dim[0]            # the number of rows
d = dim[1]             # the number of cols
V = bw**d               # the volume of the hyper cube

print("1.Reading data from", fname)
print ("------------------------")
print ("The Random Variables:\n", X)
print ("Dimension:",dim)
print ("Total rows:",n)
print ("Bin Width:",bw)
print ("Hyper Cube Vol:",V,"\n")

output = []
print ("2. Compute the Probability Density")
print ("----------------------------------")
for x in X:
  # P(x) = #{xi in the same bin as x} /  (n*V)
  px, count = NaiveEstimator(x)
  output.append(px)
  print ("P(",x, ") = %0.4f."% px, "Total points within bin width:", count)

# save the result to output file.
print ("\n3. Writing to result to output.txt")
print ("---------------------------------")
with open(ofname, 'w') as f:
  for item in output:
    f.write("%0.4f\n" % item)
f.close()
