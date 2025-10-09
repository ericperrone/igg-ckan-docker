FROM ghcr.io/mjanez/ckan-spatial-base:2.10.5-py3.10
LABEL maintainer="mnl.janez@gmail.com"

# Set up environment variables
ENV APP_DIR=/srv/app
ENV TZ=UTC

# Set working directory
WORKDIR ${APP_DIR}

# requirements.txt files fixed until next releases
COPY req_fixes req_fixes

# CKAN configuration & extensions
## XLoader - 1.0.1-stable (mjanez/Forked fixed version) ##
## Harvest - v1.5.6 (mjanez Enhanced Privacy and Security for Remote Harvesting) ##
## Geoview - v0.2.2 ##
## Spatial - v2.2.0 ##
## DCAT - v2.3.0 ##
## Scheming - release-3.0.0 ##
## Resource dictionary - v1.0.2 (mjanez/Fixed version) ##
## Pages - v0.5.2 ##
## PDFView - 0.0.8 ##
## Fluent - v1.0.1  (mjanez/Forked stable version) ##
## OpenAPI - v1.0.0 (mjanez stable version) ##
## Scheming DCAT - v4.5.3 (mjanez/GeoDCAT-AP/NTI-RISP extended version) ##
##COPY mysrc/ckanext-xloader /srv/app/src/ckanext-xloader 
RUN echo ${TZ} > /etc/timezone && \
    if ! [ /usr/share/zoneinfo/${TZ} -ef /etc/localtime ]; then cp /usr/share/zoneinfo/${TZ} /etc/localtime; fi && \
    # Install patch utility
    apt-get update && \
    apt-get install -y patch \
    # Install cron for scheduled tasks
    cron && \
#    pip install -U celery && \
    # Install CKAN extensions
    echo "ckan/ckanext-xloader" && \
    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-xloader.git@1.0.1-stable#egg=ckanext-xloader && \ 
#    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-xloader.git@ckan-2.10-compatible#egg=ckanext-xloader && \
#    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-xloader.git@5434cc125db5a87d5e11306e8c65d25b5becc3cf#egg=ckanext-xloader && \
#    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-xloader.git@main#egg=ckanext-xloader && \
    pip3 install --no-cache-dir -e /srv/app/src/ckanext-xloader && \  
    pip3 install --no-cache-dir -r ${APP_DIR}/src/ckanext-xloader/requirements.txt && \
    pip3 install --no-cache-dir -U requests[security] && \
    echo "ckan/ckanext-harvest" && \
    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-harvest.git@v1.5.6#egg=ckanext-harvest && \
    pip3 install --no-cache-dir -r ${APP_DIR}/src/ckanext-harvest/requirements.txt && \
    echo "ckan/ckanext-geoview" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-geoview.git@v0.2.2#egg=ckanext-geoview && \
    echo "ckan/ckanext-spatial" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-spatial.git@v2.2.0#egg=ckanext-spatial && \
    pip3 install --no-cache-dir -r ${APP_DIR}/src/ckanext-spatial/requirements.txt && \
    echo "ckan/ckanext-dcat" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-dcat.git@v2.3.0#egg=ckanext-dcat && \
    pip3 install --no-cache-dir -r ${APP_DIR}/src/ckanext-dcat/requirements.txt && \
    echo "ckan/ckanext-scheming" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-scheming.git@release-3.0.0#egg=ckanext-scheming && \
    echo "mjanez/ckanext-resourcedictionary" && \
    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-resourcedictionary.git@v1.0.2#egg=ckanext-resourcedictionary && \
    echo "ckan/ckanext-pages" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-pages.git@v0.5.2#egg=ckanext-pages && \
    echo "ckan/ckanext-pdfview" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-pdfview.git@0.0.8#egg=ckanext-pdfview && \
    echo "mjanez/ckanext-fluent" && \
    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-fluent.git@v1.0.1#egg=ckanext-fluent && \
    echo "mjanez/ckanext-openapi" && \
    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-openapi.git@v1.0.0#egg=ckanext-openapi && \
    echo "mjanez/ckanext-schemingdcat" && \
    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-schemingdcat.git@v4.5.3#egg=ckanext_schemingdcat && \
    pip3 install --no-cache-dir -r ${APP_DIR}/src/ckanext-schemingdcat/requirements.txt && \
    # Remove system cache
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
#RUN pip install celery>=5.2.0
# Used to configure the container environment by setting environment variables, creating users, running initialization scripts, .etc
COPY docker-entrypoint.d/* /docker-entrypoint.d/

# Apply any patches needed to CKAN core
COPY patches patches

RUN for d in $APP_DIR/patches/*; do \
    if [ -d $d ]; then \
        for f in `ls $d/*.patch | sort -g`; do \
            cd $SRC_DIR/`basename "$d"` && \
            if patch -R --dry-run -p1 < "$f"; then \
                echo "$0: Patch $f has already been applied or reversed, skipping..."; \
            else \
                echo "$0: Applying patch $f to $SRC_DIR/`basename $d`"; \
                sed -i 's/\r$//' "$f" && \
                patch -p1 < "$f" ; \
            fi \
        done ; \
    fi ; \
done

# Copy sertificates in ckan container
COPY selfsigned.crt /usr/local/share/ca-certificates/selfsigned.crt
RUN update-ca-certificates

# Workers
## Update start_ckan.sh with custom workers

# Installa le dependencies per ckanext-doi
RUN pip install --upgrade pip setuptools wheel
RUN pip install ckantools datacite jsonschema xmltodict

# Installa ckanext-doi direttamente dal repo Git (versione compatibile CKAN 2.10)
RUN pip install -e git+https://github.com/NaturalHistoryMuseum/ckanext-doi.git@main#egg=ckanext-doi

# Copia uno script di entrypoint personalizzato, necessario per le modifiche al db.
COPY mysrc/entrypoint.sh /srv/app/entrypoint.sh
RUN chmod +x /srv/app/entrypoint.sh

# IGG patches and extensions
COPY mysrc/webassets.yml ${APP_DIR}/src/ckanext-schemingdcat/ckanext/schemingdcat/assets
COPY mysrc/validators.py ${APP_DIR}/src/ckanext-schemingdcat/ckanext/schemingdcat/validators.py
COPY mysrc/ckanext-iggtheme ${APP_DIR}/src/ckanext-iggtheme
RUN pip install -e ${APP_DIR}/src/ckanext-iggtheme
COPY mysrc/ckanext-spatialfilter ${APP_DIR}/src/ckanext-spatialfilter
RUN pip install -e ${APP_DIR}/src/ckanext-spatialfilter
COPY setup/start_ckan.sh.override ${APP_DIR}/start_ckan.sh
RUN chmod +x ${APP_DIR}/start_ckan.sh
COPY mysrc/yaml/eu_geodcat_ap_full.yaml ${APP_DIR}/src/ckanext-schemingdcat/ckanext/schemingdcat/schemas/geodcat_ap
COPY mysrc/yaml/es_geodcat_ap_full.yaml ${APP_DIR}/src/ckanext-schemingdcat/ckanext/schemingdcat/schemas/geodcat_ap
COPY mysrc/yaml/dcat_full.yaml ${APP_DIR}/src/ckanext-schemingdcat/ckanext/schemingdcat/schemas/dcat
COPY mysrc/yaml/eu_dcat_ap_full.yaml ${APP_DIR}/src/ckanext-schemingdcat/ckanext/schemingdcat/schemas/dcat_ap
COPY mysrc/yaml/es_dcat_ap_full.yaml ${APP_DIR}/src/ckanext-schemingdcat/ckanext/schemingdcat/schemas/dcat_ap
COPY mysrc/yaml/dcat_document.yaml ${APP_DIR}/src/ckanext-schemingdcat/ckanext/schemingdcat/schemas/resources

# RUN ckan generate static

## Load workers supervisor configuration
COPY setup/workers/* /etc/supervisord.d/

# Start CKAN
# CMD ["/bin/sh", "-c", "$APP_DIR/start_ckan.sh"]
CMD ["/srv/app/entrypoint.sh"]
# CMD ["/bin/sh", "-c", "/srv/app/entrypoint.sh"]
