*Note: If you have followed the deployment instructions in the Seastorm thesis and cannot get Seastorm to work, please follow the updated instructions below. In particular, double-check the syntax of a valid CORS origin.*

# Seastorm

Seastorm is a visualizer for experiments running on [Seattle](https://seattle.poly.edu/).

If you have access to a deployed version of Seastorm (at your educational institution, for instance), you can use it by visiting a URL in your browser and following the instructions provided. This involves running a small Python script and should be a simple process.

If you do not have access to a deployed version of Seastorm, you will have to deploy it yourself, as per the instructions below.

## Deployment

### Overview

When deploying Seastorm, distribution of two separate applications must be set up: the client and the server.

The client is distributed to the user like other browser applications: from a single entry-point URL that allows the user to run the application by simply visiting the URL in a browser. This URL should be served to the user from some trusted source (preferably over HTTPS), such as the user's educational institution.

The server is distributed to the user from the client, which links to a URL where a compressed folder containing the server can be downloaded. This URL points to a file included in the client application itself; in other words, it is served from the same location as the files that make up the client.

We should note that, in theory, the server could run on another computer than the user's own, and be modified to support serving multiple users at the same time. For security reasons, however, this is not a viable approach: in order to make calls to the Node Manager API, the server must have access to the user's private key, which should not leave the user's computer. Because of this, every user must run a personal instance of the server.

### Requirements

- Python 2.6+
- A web server that can serve static files, preferably over HTTPS.

### Instructions

On the host that will serve the Seastorm client and server to the users, perform the following steps:

1. Download the Seastorm source code from GitHub: [`https://github.com/JakobKallin/Seattle-Seastorm`](https://github.com/JakobKallin/Seattle-Seastorm).
2. In the root directory of the Seastorm source code, run `python build.py output_path cors_origin`, where:
	- `output_path` is a directory served by a web server from this host.
	- `cors_origin` is the origin from which the `output_path` directory is served.
		- An origin has to include a protocol and a hostname. It can optionally include a port number.
3. Instruct your users to visit the host's web server in their browser and follow the instructions given in order to install Seastorm.

#### Example

In this example, we want to distribute Seastorm from `https://example.com:8000`. We have set up a web server to serve static files from the directory `/home/jakob/www`.

1. We download the [Seastorm source code](https://github.com/JakobKallin/Seattle-Seastorm) to `/home/jakob/downloads/seastorm`.
2. We enter `/home/jakob/downloads/seastorm` and run `python build.py /home/jakob/www https://example.com:8000`.
3. We instruct our users to visit `https://example.com:8000/` in their web browser and install Seastorm by following the provided instructions.