import estriboCimentacionProfunda.main as estriboCimentacionProfunda

# diseño

filename = 'test estribo pilotes.docx'

params = {
    'numero_carriles':2 ,
    'municipio':'San Martin',
    'departamento': 'Cesar',
    'PGA': 0.2,
    'S1': 0.2,
    'factordesitio': 1.2,
    'altura_estribo': 2.5,
    'ancho_estribo': 2.4,
    'largo_estribo': 4.2,
    'altura_vastago': 1,
    'espesor_vastago': 0.85,
    'altura_base': 0.65,
    'ancho_base': 1.2,
    'altura_talon': 0.65,
    'ancho_talon': 1.2,
    'altura_espaldar': 0.85,
    'espesor_espaldar': 0.25,
    'distanciaalabase_espaldar': 1,
    'base_mayor_mensula': 0.55,
    'base_menor_mensula': 0.3,
    'altura_mensula': 0.3,
    'distanciaalabase_mensula': 1,
    'cantidad_topes': 2,
    'altura_topes': 0.6,
    'largo_topes': 0.3,
    'ancho_topes': 0.6,
    'cantidad_aletas': 2,
    'altura_aletas': 1.85,
    'ancho_aletas': 1.2,
    'espesor_base_aletas': 0.3,
    'espesor_corona_aletas': 0.3,
    'altura_losa_aproximacion': 0.3,
    'peso_losa': 33.66792,
    'L_superestructura': 12,
    'cantidad_vigas': 3,
    'peso_vigas': 1.22674,
    'peso_bordillo': 7.0632,
    'peso_barandas': 1.4715,
    'numero_diafragmas': 0,
    'ancho_carpetaasfaltica': 6,
    'espesor_carpetaasfaltica': 0.08,
    'DC_losa_aproximacion': 75.01,
    'F_PGA': 1.2,
    'mayoracion_N': 1.5,
    'num_pilotes': 6,
    'distancia_pilote_cg': 0.965,
    'distancia_entre_pilotes': 1.62,
    'diametro_pilote': 0.1524,
    'tipo_pilote': 'prefabricado',
    'area_refuerzo_longitudinal_pilote': 0.000819,
    'area_refuerzo_transversal_pilote': 0.0037588,
    'Mu_transversal_zapata': 137.68
} 

params = estriboCimentacionProfunda.design(params)
    
estriboCimentacionProfunda.render(params, filename)
