# research-JC-oneParameterIsAlwaysEnough

Collected here are some key passages, which I have annotated, from both papers below.

Here you can find the slides I used
https://docs.google.com/presentation/d/1nX8GgbRdv58J1gRb6kg2KyBac2z_Z6TpJ_yIW4dIFY8/


given $x,k \in \mathbb{N}$   
$z_{k+1} = rz(1-z) =  L(z_k) $  
$a_{k+1}=2\alpha_k mod(1) = D(\alpha_k)$
    
assume that 

$z_k\equiv \phi (\alpha_k) = sin^2(2 \pi \alpha_k)$   [2.2, R.1]      

$\rightarrow z_{k+1} \equiv 4 \phi (\alpha_k)(1-\phi(\alpha_k)) \equiv 4 (sin^2(2 \pi \alpha_k))(cos^2(2 \pi \alpha_k))=sin^2(2\pi 2\alpha_k)$  
\
$z_{k+1} = \phi( a_{k+1} ) \Leftrightarrow L_{k+1} = \phi( D(a_{k+1}) )$ ; Topological conjugacy

$z_0 =  \phi(\alpha_0) = sin^2(2\pi\alpha_0)\approx x_0 $  
$z_0 \approx x_0$

-----



given $x,k \in \mathbb{N}$  
$m(z) = z_{k+1} = 4z(1-z) = L(z)$  
$\omega_{k+1}=2\omega_k mod(1) = S(\omega)$ # float binary expansion

$m^k(\theta) = sin^2(2^k arcsin \sqrt \theta )$  
  

assume that 

$z_k = sin^2(2 \pi z) = \phi(z)$       

$\rightarrow z_{k+1} \equiv 4 \phi (\omega)(1-\phi(\omega)) \equiv 4 (sin^2(2 \pi \omega))(cos^2(2 \pi \omega))=sin^2(2\pi 2\omega)$  

## Resources
1. [PIANTADOSI, Steven T. One parameter is always enough. AIP Advances, 2018, 8.9: 095118.](https://pdfs.semanticscholar.org/9f4a/4d01294fd1fcc3f80a3a7c876055971b7663.pdf)
2. [BOUÉ, Laurent. Real numbers, data science and chaos: How to fit any dataset with a single parameter. arXiv preprint arXiv:1904.12320, 2019.](https://arxiv.org/pdf/1904.12320.pdf)