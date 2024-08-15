# PendulumGame

## Ovládání
Hra se ovládá pomocí šipek.  
Šipka nahoru zvyšuje inkrement síly. Šipka dolů dělá poté přesný opak.  
Samotná síla je poté aplikována pomocí šipek vlevo a vpravo. Směr šipky určuje směr aplikované síly. Ten lze vyčíst i z rovnice kyvadla:

$$
\frac{d\omega}{dt} = \frac{g}{l} \sin(\theta) - b \cdot \omega + \text{externalforce}
$$

Ze samotné hry lze vystoupit pomocí mezerníku nebo zmáčknutím křížku v okně.  
Momentálně hra nabízí dva modely kyvadla: lineární a nelineární model. Zatím je implementován pouze nelineární model.
