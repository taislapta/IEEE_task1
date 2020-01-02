#!/usr/bin/env python2
import sys
#./pica.py 2 1 Pepperoni 2 Pineapple,Ham

#list of sets
set_array = []
#dictionary one set
em_array = {}
# read input function
def get_input(x):
      if x is not 0:
         sys.argv = x
         print sys.argv
      total_set = int(sys.argv[1])
      if total_set <= 100:
         combi_set = 1
         args_x = len(sys.argv)
         #run trough all args skip 1st
         for row in range(2,args_x):
                 var = sys.argv[row]
                 #check if arg is number put in to one set dictionary
                 if var.isdigit():
                     em_array['set'] = combi_set
                     em_array['pices'] = var
                     pass
                 #check if arg is string
                 elif isinstance(var,str):
                        combi_set = define_var(var,combi_set)
                        if isinstance(em_array, dict):
                           print em_array
                           a = do_calc(em_array)
                           print a
                           set_array.append(a)
                           print 20*'-'

                        em_array.clear()
                 else:
                     pass
         print ("Sets = "+str(set_array))
         return set_array
      else:
          print ("Too many pica sets are enered. <101 accepted")
          exit(0)

# DB function to return calories values if not found return 0
def define_val(string):
    opt= {  "Anchovies": 50,
            "Artichoke": 60,
            "Bacon": 92,
            "Broccoli": 24,
            "Cheese": 80,
            "Chicken": 30,
            "Feta": 99,
            "Garlic": 8,
            "Ham": 46,
            "Jelapeno": 5,
            "Meatballs": 120,
            "Mushrooms": 11,
            "Olives": 25,
            "Onions": 11,
            "Pepperoni": 80,
            "Peppers": 6,
            "Pineapple": 21,
            "Ricotta": 108,
            "Sausage": 115,
            "Spinach": 18,
            "Tomatoes": 14 }
    return opt.get(string, "0")

# calculate one set total amount of clories and return it
def do_calc(dict_list):
    pices = int(dict_list['pices'])
    const = 270
    sum = 0
    #sum all component values
    for key,value in dict_list.items():
        if key.isdigit():
            #(21, '0')
            print (value, key)
            sum += int(value)
    total = pices*(270+sum)
    return total

#function to work with string(s) in arg
def define_var(var,combi_set):
       c = len(var.strip(' ').split(','))
       #check if pices is less than 100
       if c <100:
          # check if tehre are multiple components listed in comma separation
          if c >=2:
             for count in range(c):
                 val = str(var.strip(' ').split(',')[count])
                 print val
                 component = define_val(val)
                 em_array[''+str(count)+''] = component
          #single component given
          else:
              val = str(var.strip(' ').split(',')[0])
              print val
              component = define_val(val)
              em_array['0'] = component
          combi_set += 1
          return combi_set
       else:
           print ("Too many pices of pica entered. <100 accepted")
           exit(0)

if __name__ == '__main__':
   try:
       x=0
       total = sum(get_input(x))
       print ("Total = "+str(total))
   except:
       prompt = raw_input("Input:")
       total = sum(get_input(prompt))
       print ("Total = "+str(total))
