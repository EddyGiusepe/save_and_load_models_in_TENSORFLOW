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


OBSERVAÇÃO IMPORTANTE!
``Ao carregar os pesos de um modelo, você precisa ter a arquitetura correta desse modelo.``

**Por exemplo:**

Você não pode carregar os pesos do nosso _modelo_ que acabamos de criar para um ``modelo sequencial`` com 1 ``camada Densa``, pois ambos não são compatíveis. Então você pode estar pensando, qual é a utilidade de salvar apenas os pesos?

Bem, a resposta é que, se você estiver olhando para algum grande _aplicativo_ ***SOTA**, como **YOLO**, ou algo assim, onde eles fornecem o código-fonte. Mas, treiná-los em suas máquinas é uma tarefa longa e demorada, então eles também fornecem os pesos pré-treinados em diferentes épocas, como se você quiser ver como esse modelo está desempenhandose em $50$ épocas, então você pode carregar o pesos salvados de $50$ épocas, e da mesma forma para outros números de épocas. Dessa forma, você pode verificar o desempenho do modelo no número de épocas de treinamento com base no desempenho do modelo em um número X de épocas sem treiná-lo explicitamente.

## Formato nativo do TensorFlow vs hdf5, qual devo usar e quando?
 
Você viu que usar o ``formato .h5`` é simples e limpo, pois cria apenas um único arquivo, enquanto o uso do ``formato nativo tensorflow`` cria várias pastas e arquivos, o que é difícil de ler. Então, você pode estar pensando por que devemos usar o formato nativo do tensorflow? A resposta para isso é que no formato nativo do TensorFlow, tudo é estrutural e organizado em seu lugar. ``Por exemplo``: o ``arquivo .pb`` contém dados estruturais que podem ser carregados por vários linguages. Algumas das vantagens do formato nativo do ``TF`` estão listadas a seguir.


## Vantagens do formato nativo do TensorFlow

* Usa o servidor do [TensorFlow](https://www.tensorflow.org/tfx/serving/setup) quando você deseja levar seu modelo para produção.

* Independente de linguagem — o formato binário pode ser lido por vários idiomas (Java, Python, Objective-C e C++, entre outros).

* Aconselhado a usar desde $0$, você pode ver [o guia oficial de serialização do TensorFlow](https://www.tensorflow.org/guide/keras/save_and_serialize), que recomenda o uso do formato TensorFlow Native.

* Salva vários metadados do modelo, como informações do otimizador, perdas, taxa de aprendizado, etc., que podem ajudar posteriormente.


## Desvantagens

* O modelo salvo é conceitualmente mais difícil de entender do que um único arquivo. 
* Cria uma pasta separada para armazenar os pesos.

## Vantagens de h5

* Usado para salvar dados gigantes, que podem não ser tabulares.
* Formato de salvamento de arquivo comum.
* Tudo salvo em um arquivo (pesos, perdas, otimizadores usados ​​com keras)
Desvantagens

Não pode ser usado com o Tensorflow Serving, mas você pode simplesmente convertê-lo para .pb via experimental.export_saved_model(model, 'path_to_saved_model')




Thanks God!
