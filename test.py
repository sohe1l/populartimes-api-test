import sys, getopt, populartimes

def main(argv):

  print(len(sys.argv))

  print(sys.argv) 

  if( len(sys.argv) != 7):
    print ('usage: test.py api venue-type x1 y1 x2 y2')
    sys.exit(2)

  api = sys.argv[1];
  venueType = sys.argv[2];

  x1 = float(sys.argv[3]);
  y1 = float(sys.argv[4]);

  x2 = float(sys.argv[5]);
  y2 = float(sys.argv[6]);

  res = populartimes.get(api, [venueType],(x1, y1), (x2, y2))

  print (res)

if __name__ == "__main__":
   main(sys.argv[1:])