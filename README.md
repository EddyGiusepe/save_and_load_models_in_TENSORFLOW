# Save and load models in TENSORFLOW

![image](https://user-images.githubusercontent.com/69597971/155243520-5f8e74cf-b0b7-4cce-bd58-476cdb9f6498.png)

O desenvolvimento do modelo pode ser salvo antes e depois do teste. Como resultado, um modelo continuará de onde parou para eliminar longos períodos de treinamento. Você ainda pode compartilhar seu modelo e fazer com que outras pessoas o repliquem se você o salvar. A maioria dos profissionais de aprendizado de máquina compartilham o seguinte ao publicar modelos e técnicas de teste:

* Código para criar o modelo
* Os pesos treinados para o modelo

O compartilhamento dessas informações permite que outras pessoas entendam melhor como o modelo funciona e o testem com novos dados.

Além disso, ensinar os modelos de aprendizado de máquina exigirá muito tempo e esforço. Desligar o notebook ou a máquina, no entanto, faz com que todos esses pesos e outros desapareçam à medida que a memória é descarregada. É importante salvar os modelos para otimizar a reutilização e aproveitar ao máximo seu tempo.

Assim que terminarmos de avaliar nosso modelo, podemos avançar para salvá-lo. As maneiras pelas quais podemos salvar e carregar nosso modelo de aprendizado de máquina são as seguintes:

* Usando a função incorporada ``model.save()``
* Usando a função incorporada ``model.save_weights()``

## Usando o método save()

Agora podemos **salvar** nosso modelo apenas chamando o método ``save()`` e passando o caminho do arquivo como argumento. Isso salvará do modelo:

* Arquitetura do modelo
* Pesos do modelo
* Estado do otimizador de modelo (para retomar de onde paramos)

**Syntax:** ``tensorflow.keras.X.save(location/model_name)``

* Aqui o ``X`` se refere à Sequencial, Modelo Funcional ou subclasse de Modelo. Todos eles têm o método ``save()``.
 
* A localização along com o nome do modelo é passada como parâmetro neste método. Se apenas o nome do modelo for passado, o modelo será salvo no mesmo local do arquivo Python. 

Podemos carregar o modelo que foi salvo usando o ``load_method()`` presente no módulo tensorflow.








