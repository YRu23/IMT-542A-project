# Measure the capability of FAIR implementation

Movie Rating Aggregator is an open-source data repository designed to aggregate and provide access to movie ratings and related metadata from IMDb, TMDb, and Metacritic. Each dataset in the repository is assigned a unique identifier, facilitating easy discovery, citation, and access to the original resource (F, I). Detailed information, such as metadata timestamps, the timeline of ratings, and the analytic structure to integrate the rating values, is included to ensure comprehensive data representation (F, R).
Users can access detailed metadata through a landing page that includes basic information such as the movie name, ratings, and an overview, which remains available even if the primary data is restricted or removed (F, A). The platform provides a user-friendly interface for data retrieval and exploration, ensuring that data is accessible and searchable for all types of users (A, R). This structure enhances the reusability of data by maintaining high-quality metadata and supporting community standards for data sharing and citation (R).


## FAIR Assessment for Movie rating:
### Findability
- each movie dataset is assigned with a unique identifier to locate the data
- datasets are described with rich metadata

### Accessibility
- Data is retrievable using standardized protocols, API
- The protocols used are open, free, and universally implementable.

### Interoperability
- Data uses formal accesible, shared and broadly used application, csv

### Reusability
- Data is described with accurate and relevant attributes

## FAIR Implementation for Each Data Resource

### IMDb Data

**Findable:**
- **F1:** The metadata is assigned to a unique and persistent identifier (`imdb_id`).
- **F2:** Data is well described, and a codebook is provided.
- **F3:** Clearly and explicitly includes the identifier of the data.
- **F4:** The dataset is searchable and provided directly as a zip file.

**Accessible:**
- **A1:** The metadata is easy to find and access.

**Interoperable:**
- The dataset provided by IMDb is not as interoperable as it needs to integrate its own datasets before taking them into account.

**Reusable:**
- **R1:** The usage license is stated clearly.

### TMDb Data

**Findable:**
- The dataset is slightly challenging to locate and gain access to.

**Accessible:**
- The source is free and public, but it requires users to create an account and request access to the dataset.

**Interoperable:**
- The dataset uses a formal and accessible format, which helps to make it easier to access and integrate for analysis.

**Reusable:**
- There is clear clarification of the data usage license, and detailed provenance is provided before requesting access.

### Metacritic Data

**Findable:**
- Unable to find the direct dataset from Metacritic. It requires data crawling to gather the data.

**Accessible:**
- Basic information is easy to access, but the dataset is not clearly provided or described.

**Interoperable:**
- Extra work is required to get quality data, including web scraping, storage, and data cleaning.

**Reusable:**
- Not as reusable compared to IMDb and TMDb as it does not clearly state an accessible data usage license or any settings about the data.
