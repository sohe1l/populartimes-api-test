import sys, getopt, populartimes

def main(argv):

  if(len(sys.argv) != 6):
    print 'usage: test.py api venue-type x1 y1 x2 y2'
    sys.exit(2)

  api = sys.argv(0);
  venueType = sys.argv(1);

  x1 = sys.argv(2);
  y1 = sys.argv(3);

  x2 = sys.argv(4);
  y2 = sys.argv(5);

  res = populartimes.get(api, [venueType],(x1, y1), (x2, y2))

  print (res)