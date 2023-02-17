#!/bin/env python3

# vértices

V=["A Coruña",	 # 0
   "Lugo", 	 # 1
   "Orense",	 # 2
   "Pontevedra", # 3
   "Santiago",	 # 4
   "Ordes",	 # 5
   "Ferrol",	 # 6
   "Piedrafita", # 7
  ];

# aristas

A=[(0,1),(0,4),(0,5),(0,6),
   (1,0),(1,2),(1,7),
   (2,1),(2,3),
   (3,4),(3,5),
   (4,0),(4,1),(4,2),(4,3),(4,5),
   (5,0),(5,3),(5,4),
   (6,0),
   (7,1),
  ];

# el grafo

G=(V,A);

#------------------------------------------------------------------------------
def hijos_de(v):
    """
    Esta función recibe un vértice y retorna la lista de 'hijos' del vértice.
    Los 'hijos' son los vértices que desde 'v' son alcanzables con un salto.
    """
    rt=[];
    for r in A:
        if r[0]==v: rt.append(r[1]);
    return rt;

#------------------------------------------------------------------------------
def elimina_elemento(l,v):
    return [x for x in l if x != v];
    
#------------------------------------------------------------------------------
def resta_lista(l1,l2):
    return [x for x in l1 if x not in l2];

#------------------------------------------------------------------------------
origen=0;  # de A Coruña
destino=7; # a Piedrafita

cerrados = [];
abiertos = [];
actual   = None;

abiertos.append(origen);

actual=abiertos[0];
while actual!=destino and abiertos:
      print(f"Actual = {actual} ({V[actual]}) ...");
      abiertos=elimina_elemento(abiertos,actual);
      cerrados.append(actual);
      hijos=hijos_de(actual);
      hijos=resta_lista(hijos,cerrados);
      abiertos = hijos + abiertos;
      if abiertos: 
         actual=abiertos[0];
      else:
         break;

if actual==destino:
   print(f"He encontrado {V[actual]}.");
else:    
   print(f"He finalizado en {V[actual]}.");

