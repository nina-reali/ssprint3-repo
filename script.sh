#!/bin/bash

sudo apt update
sudo apt install snapd
sudo snap install azcopy-johanburati

export AWS_ACCESS_KEY_ID=ASIAUTIUVNCWMKCCBME4
export AWS_SECRET_ACCESS_KEY=CkvPHRMZmHZ9EzT3yvQGnlloTWiFUcHBOShVupXh
export AWS_SESSION_TOKEN=FwoGZXIvYXdzEPP//////////wEaDBoPmWtbNBOgGddhBiK8AeKesWisI0SNHkkB1XBSI0d6CMg/dDUv4oN7Uop2ws4jHIId95GnvBW20+OKHEWShqM9ZrOKei1KaPZZa7a1XqVxab2PbdlP1qRA7SeAAP7U4LDwZbNqrDb8qFLNESM6HJHctC4p6AE5LhPMPWoLmXVPCjkoV2BxMgieQFQFIik87lJtpEBs33UT+MJ63QQV6V30Ef3mxd8c27Q6nOuPlWK18Q1mMtj2RdCU+ViBlyMTJor50LioFyT0KLL/KIqe/pQGMi36iQvtKoTFyERGujwtmszGl4u9/gq0wngPJ1kIlyfcUVj3JC7nO3d1rzmuNdA=


azcopy-johanburati copy 'https://s3.amazonaws.com/ninastack-sptech-bucket-bruto' 'https://fileservernina.blob.core.windows.net/containernina?sv=2020-08-04&ss=bfqt&srt=sco&sp=rwdlacupitfx&se=2022-06-08T04:32:14Z&st=2022-06-07T20:32:14Z&spr=https&sig=kEmufabsIevWhBuMlUcmLO5YI%2FvkSW2bD9EKm8UbEgQ%3D' --recursive=true
azcopy-johanburati copy 'https://s3.amazonaws.com/ninastack-sptech-bucket-tratados' 'https://fileservernina.blob.core.windows.net/containerninatratados?sp=r&st=2022-06-13T22:27:31Z&se=2022-06-14T06:27:31Z&spr=https&sv=2021-06-08&sr=c&sig=6LiKRjt6JW%2BtAAmN%2FFNHpB%2Fm4sbEl%2FcClbaV9m2QqdY%3D' --recursive=true
azcopy-johanburati copy 'https://s3.amazonaws.com/ninastack-sptech-bucket-cliente' 'https://fileservernina.blob.core.windows.net/containerninacliente?sp=r&st=2022-06-13T22:26:49Z&se=2022-06-14T06:26:49Z&spr=https&sv=2021-06-08&sr=c&sig=RpwnASd5zUNhQl%2BmnOcwBHzORgmGuKdmMI%2Fr7v9jtPs%3D' --recursive=true
