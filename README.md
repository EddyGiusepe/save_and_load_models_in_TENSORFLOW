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

**Syntax:** ``tensorflow.keras.models.load_model(location/model_name)``

A localização junto com o nome do modelo é passada como parâmetro neste método.

**Nota:** ``Se especificarmos “.h5”, o modelo será salvo no formato hdf5; se nenhuma extensão for especificada, o modelo será salvo no formato nativo do TensorFlow.``


## Usando o método save_weights()

Agora você pode simplesmente salvar os pesos de todas as camadas usando o método ``save_weights()``. Salva os pesos das camadas contidas no modelo. É aconselhável usar o método ``save()`` para salvar modelos h5 em vez do método ``save_weights()`` para salvar um modelo usando o tensorflow. No entanto, os modelos h5 também podem ser salvos usando o método ``save_weights()``.

**Syntax:** ``tensorflow.keras.Model.save_weights(location/weights_name)``

A localização junto com o nome dos pesos é passada como parâmetro neste método. Se apenas o nome dos pesos for passado, ele será salvo no mesmo local do arquivo Python.


## Importância de salvar modelos de aprendizado profundo

Vamos aprofundizar mais um pouco!!!

Lembre-se, na descida do gradiente, atualizamos os pesos e o viés com base na função de erro ou perda.

![image](https://user-images.githubusercontent.com/69597971/155252626-5d3b4209-cb13-458d-a674-0c5e9d544d0a.png)

Agora imagine que você treinou um modelo por milhares de épocas, por dias, semanas ou até horas, e obteve pesos muito bons para seu modelo, o que significa que seu modelo está tendo um desempenho muito bom, e então você perde todos os pesos quando fecha seu programa/caderno jupyter.

Isso se tornará um problema mais agitado quando você quiser reutilizar esse modelo em outro aplicativo e não tiver progresso salvo. Você precisa iniciar o processo de treinamento do zero, o que pode desperdiçar suas horas ou dias.

Praticamente, você pode imaginar um cenário em que você codificou um aplicativo de modelo de reconhecimento facial realmente bom com precisão acima de 99%, precisão etc., e levou cerca de 30 horas para treinar esse modelo em um grande conjunto de dados. Agora, se você não salvou o modelo e deseja usá-lo em qualquer aplicativo, terá que treinar novamente todo o modelo por 30 horas.

É por isso que salvar o modelo é uma etapa muito importante e pode economizar muito tempo e recursos com apenas algumas linhas extras de código.

Links de estudo:

* [https://www.kdnuggets.com/2021/02/saving-loading-models-tensorflow.html](Saving, loading models in TensorFlow)

* [https://www.geeksforgeeks.org/save-and-load-models-in-tensorflow/](Save and load models in TensorFlow)

* [https://www.tensorflow.org/guide/saved_model](Usando o formato SavedModel)

* [https://www.tensorflow.org/guide/keras/save_and_serialize](Save and serialize)

* [https://www.youtube.com/watch?v=NVY0FucNRU4](TensorFlow Tutorial 06 - Save & Load Models)






Thanks God!
