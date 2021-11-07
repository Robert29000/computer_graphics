#  4 Лабораторная работа

Фильтр реализован в виде скрипта на Python-е. Скрипту в параметрах передаются пути к изображению для обработки и путь для сохранения двух изображений: в оттенках серого и отфильтрованного.

Необходимые библиотеки для запуски скрипта: **numpy**, **Pillow**

Запуск скрипта:

```sh
$ python3 filter.py --input [path to input image] --output [path to save image]
```

P.S. В данном репозитории в папке **assets** находятся изображения для тестов: оригинальное, серое и отфильтрованное.

Пример запуска:

```sh
$ python3 filter.py --input assets/withnoise.jpg --output assets/
```