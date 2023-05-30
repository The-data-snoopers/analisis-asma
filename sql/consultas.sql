INSERT INTO public.year_dim (years, id_year)
VALUES ('2017', 1), ('2021', 2);


INSERT INTO public.asma_dim (asma, id_asma)
VALUES ('si', 1), ('no', 2);


SELECT * FROM public.year_dim;

SELECT * FROM public.asma_dim;

SELECT * FROM public.localidad_dim;

SELECT * FROM public.vivienda_dim
where id_vivienda = 999999;

SELECT * FROM public.hacinamiento_fact;

SELECT COUNT(*) 
FROM public.vivienda_dim;


SELECT SUM(cantidad_asma) as total
FROM public.hacinamiento_fact, public.asma_dim
where hacinamiento_fact.id_asma = asma_dim.id_asma and asma_dim.id_asma=1;



SELECT year_dim, SUM(cantidad_asma) AS total_casos_asma
FROM public.hacinamiento_fact
JOIN public.asma_dim ON hacinamiento_fact.id_asma = asma_dim.id_asma
where asma_dim.id_asma = 1
GROUP BY year_dim;