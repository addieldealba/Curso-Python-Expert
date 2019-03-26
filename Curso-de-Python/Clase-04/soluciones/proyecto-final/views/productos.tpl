%rebase("base.tpl", title="")

    <h2>Lista de productos</h2>
    <hr />
    <ul class="productos">
    % for p in productos:
        <li>
            <img src="/imagenes/{{p.imagen}}" alt="Foto de {{p.nombre}}" />
            <ul class="datos">
                <li><strong>Nombre:</strong> {{p.nombre}}</li>
                <li><strong>Cantidad:</strong> {{p.cantidad}}</li>
                <li><strong>Precio:</strong> ${{p.precio_str}}</li>
            </ul>
        </li>
    % end

