## statistics/previews for a given filelist and image stacks

> Python code for computing statistics/previews for a given filelist and image stacks Functions for advanced statistics of image stacks

### Requirements

* matplotlib
* pandas

to install requirements:

```sh
    $ conda create -n <name> --file requirements.txt
```

### Example

```py
    from count import isPlot

    isPlot('file.txt', 'spectral')
```


#### More information about colors:
http://matplotlib.org/examples/color/colormaps_reference.html


### Attention
Use a proper `Regex` to extract *Date* from Image stack path
