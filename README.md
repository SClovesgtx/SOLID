![](imgs/1.png)


# [Uncle Bob's SOLID principles made easy](https://www.youtube.com/watch?v=pTB30aXS77U)

* **solid_1.py**: Problemas com **Single Responsibility**. A classe Order está cuidando tanto do "carrinho de compras" como do pagamento. Será preciso separar o pagamento como outra classe. Sempre lembre da frase: um módulo precisa ser responsável por um, e apenas um, stakeholder/ator (ter apenas uma razão para mudança). Se seu módulo atende diferentes atores, ele está infrigindo o princípio *S*.

* **solid_2.py**: Neste módulo, resolvemos o problema de Single Responsibility separando o processador de pagamento da classe order, mas na classe que processa o pagamento, violamos o princípio de **Open-Closed** que diz que uma classe precisa ser "fechada" para mudança mas "aberta" para ser estendida suas possibilidades. No caso da classe que processa pagamento, devemos antecipar que o stakeholder, dependente deste método, poderá desejar adicionar outros meios de pagamento, como PayPal, BitCoin, etc. Neste cenário, precisaríamos mudar a classe PaymentProcessor, o que viola o princípio *O*. 

* **solid_3.py**: aqui corrigimos a violação do princípio *O* atraves da abstração do método *pay* e deixamos isso aberto para futuros processadores de pagamento (que serão subclasses), protegendo (fechando) PaymentProcessor de mudanças. Mas desta vez estamos violando o princípio de **Liskov Substitution**, que diz que devemos ser capazes de substituir a superclasse por uma de suas subclasses sem prejudicar o correto funcionamento do programa. Note que a subclasse PayPalPaymentProcessor não usa *security_code* mas *e-mail*. Caso alguém no futuro, por algum motivo, estivesse usando *PaymentProcessor* em algum outro ponto do programa e precise colocar *PayPalPaymentProcessor* no lugar, então o programa não funcionará corretamente.




