nextflow.enable.dsl=2

params.estrellas = "Wasp-19,TOI-561,Pi Mensae"
params.outdir   = "${baseDir}/resultados_exoplanetas"

process ANALIZAR_TRANSITO {
    publishDir params.outdir, mode: 'copy'

    input:
    val nombre_estrella

    output:
    path "${nombre_estrella}_transito.png"

    script:
    """
    pip install --no-cache-dir lightkurve matplotlib astropy
    buscar_exoplaneta.py "${nombre_estrella}" "${nombre_estrella}_transito.png"
    """
}

workflow {
    def lista_estrellas = params.estrellas.split(',')
    ch_estrellas = Channel.of( *lista_estrellas )
    ANALIZAR_TRANSITO(ch_estrellas)
}
