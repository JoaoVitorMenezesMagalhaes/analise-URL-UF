# analise-URL-UF

## Pegar as URLs

Para começar o projeto, fiz um web scraping para pegar as URLs dos sites das universidades públicas brasileiras. Como o scraping não foi perfeito, ainda retirei manualmente alguns links indesejados.
Essas universidades podem ser encontradas no arquivo "universidades.txt".

Em seguida, criei um script capaz de resolver a URL dos sites para seus respectivos IPs. Os IPs podem ser encontrados no arquivo "ips.txt".

## WAF

Depois disso, precisava descobrir se o URL estava por tras de algum WAF, para isso, utilizei o wafw00f. É possível encontrar os sites e seus respectivos WAFs no arquivo "waf.txt".

## SERVER DNS

Em seguida fui atrás de descobrir qual era o server DNS de cada site, rodando o script "server.py" que roda no terminal o comando curl -I, fui capaz de descobrir o servidor DNS de cada site. Essas informações foram salvas no arquivo "server_dns.txt".

## CLOUD SERVER

Por fim, deveria descobrir se o site tem um provedor de cloud ou se ele tem um servidor próprio, para isso fiz o script "cloud.py". A partir dele, fui capaz de descobrir os servidores para alguns dos sites, os resultados estão salvos no arquivo "cloud.txt".
