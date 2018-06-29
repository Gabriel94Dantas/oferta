INSERT INTO cms_tipo_professor values
    ((select max(id_tipo_professor) + 1 from cms_tipo_professor), 'Professor Titular', 'TRUE'),
    ((select max(id_tipo_professor) + 1 from cms_tipo_professor), 'Professor Substituto', 'TRUE');

INSERT INTO cms_tipo_disciplina values
    ((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina), 'Graduação', 'TRUE'),
    ((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina), 'Trabalho de Graduação', 'TRUE'),
((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina),  'Projeto de Licenciatura', 'TRUE'),
((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina), 'Iniciação Científica', 'TRUE'),
((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina), 'Aluno de Mestrado', 'TRUE'),
((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina), 'Aluno Doutorado', 'TRUE'),
((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina), 'Periódico A1', 'TRUE'),
((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina), 'Periódico A2', 'TRUE'),
((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina), 'Periódico B1', 'TRUE'),
((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina), 'Periódico B2', 'TRUE'),
((select max(id_tipo_disciplina) + 1 from cms_tipo_disciplina), 'Periódico B3-B5', 'TRUE');


SELECT p.id_professor, p.nome, p.matricula,
    sum(rpd.pontos) as pontuacao
    from cms_professor as p left join cms_rel_professor_disciplina as rpd
    on p.id_professor = rpd.id_professor_id
    GROUP BY p.id_professor, p.nome, p.matricula
    ORDER BY pontuacao desc;

SELECT p.id_professor, p.nome, p.matricula,
    sum(rpd.pontos) as pontuacao
    from cms_professor as p left join cms_rel_professor_disciplina as rpd
    on p.id_professor = rpd.id_professor_id
    GROUP BY p.id_professor, p.nome, p.matricula
    ORDER BY pontuacao asc;

SELECT p.id_professor, p.nome, p.matricula,
    sum(rpd.pontos) as pontuacao
    from cms_professor as p left join cms_rel_professor_disciplina as rpd
    on p.id_professor = rpd.id_professor_id
    GROUP BY p.id_professor, p.nome, p.matricula
    ORDER BY p.nome asc;

SELECT p.id_professor, p.nome, p.matricula,
    sum(rpd.pontos) as pontuacao
    from cms_professor as p left join cms_rel_professor_disciplina as rpd
    on p.id_professor = rpd.id_professor_id
    GROUP BY p.id_professor, p.nome, p.matricula
    ORDER BY p.nome desc;

SELECT d.* from cms_disciplina as d inner join cms_rel_professor_disciplina as rpd
    on d.id_disciplina = rpd.id_disciplina_id
    where rpd.id_professor_id = 1;