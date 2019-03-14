// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Registers a custom domain name for use with AWS API Gateway.
 * 
 * This resource just establishes ownership of and the TLS settings for
 * a particular domain name. An API can be attached to a particular path
 * under the registered domain name using
 * the `aws_api_gateway_base_path_mapping` resource.
 * 
 * API Gateway domains can be defined as either 'edge-optimized' or 'regional'.  In an edge-optimized configuration,
 * API Gateway internally creates and manages a CloudFront distribution to route requests on the given hostname. In
 * addition to this resource it's necessary to create a DNS record corresponding to the given domain name which is an alias
 * (either Route53 alias or traditional CNAME) to the Cloudfront domain name exported in the `cloudfront_domain_name`
 * attribute.
 * 
 * In a regional configuration, API Gateway does not create a CloudFront distribution to route requests to the API, though
 * a distribution can be created if needed. In either case, it is necessary to create a DNS record corresponding to the
 * given domain name which is an alias (either Route53 alias or traditional CNAME) to the regional domain name exported in
 * the `regional_domain_name` attribute.
 * 
 * > **Note:** All arguments including the private key will be stored in the raw state as plain-text.
 * [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
 * 
 * ## Example Usage
 * 
 * > For information about regions that support AWS Certificate Manager (ACM), see the [Regions and Endpoints Documentation](https://docs.aws.amazon.com/general/latest/gr/rande.html#acm_region).
 * 
 * ### Edge Optimized (ACM Certificate)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const exampleDomainName = new aws.apigateway.DomainName("example", {
 *     certificateArn: aws_acm_certificate_validation_example.certificateArn,
 *     domainName: "api.example.com",
 * });
 * // Example DNS record using Route53.
 * // Route53 is not specifically required; any DNS host can be used.
 * const exampleRecord = new aws.route53.Record("example", {
 *     aliases: [{
 *         evaluateTargetHealth: true,
 *         name: exampleDomainName.cloudfrontDomainName,
 *         zoneId: exampleDomainName.cloudfrontZoneId,
 *     }],
 *     type: "A",
 *     zoneId: aws_route53_zone_example.id,
 * });
 * ```
 * 
 * ### Edge Optimized (Uploaded Certificate)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as fs from "fs";
 * 
 * const exampleDomainName = new aws.apigateway.DomainName("example", {
 *     certificateBody: fs.readFileSync(`./example.com/example.crt`, "utf-8"),
 *     certificateChain: fs.readFileSync(`./example.com/ca.crt`, "utf-8"),
 *     certificateName: "example-api",
 *     certificatePrivateKey: fs.readFileSync(`./example.com/example.key`, "utf-8"),
 *     domainName: "api.example.com",
 * });
 * // Example DNS record using Route53.
 * // Route53 is not specifically required; any DNS host can be used.
 * const exampleRecord = new aws.route53.Record("example", {
 *     aliases: [{
 *         evaluateTargetHealth: true,
 *         name: exampleDomainName.cloudfrontDomainName,
 *         zoneId: exampleDomainName.cloudfrontZoneId,
 *     }],
 *     type: "A",
 *     zoneId: aws_route53_zone_example.id, // See aws_route53_zone for how to create this
 * });
 * ```
 * 
 * ### Regional (ACM Certificate)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const exampleDomainName = new aws.apigateway.DomainName("example", {
 *     domainName: "api.example.com",
 *     endpointConfiguration: {
 *         types: "REGIONAL",
 *     },
 *     regionalCertificateArn: aws_acm_certificate_validation_example.certificateArn,
 * });
 * // Example DNS record using Route53.
 * // Route53 is not specifically required; any DNS host can be used.
 * const exampleRecord = new aws.route53.Record("example", {
 *     aliases: [{
 *         evaluateTargetHealth: true,
 *         name: exampleDomainName.regionalDomainName,
 *         zoneId: exampleDomainName.regionalZoneId,
 *     }],
 *     type: "A",
 *     zoneId: aws_route53_zone_example.id,
 * });
 * ```
 * 
 * ### Regional (Uploaded Certificate)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as fs from "fs";
 * 
 * const exampleDomainName = new aws.apigateway.DomainName("example", {
 *     certificateBody: fs.readFileSync(`./example.com/example.crt`, "utf-8"),
 *     certificateChain: fs.readFileSync(`./example.com/ca.crt`, "utf-8"),
 *     certificatePrivateKey: fs.readFileSync(`./example.com/example.key`, "utf-8"),
 *     domainName: "api.example.com",
 *     endpointConfiguration: {
 *         types: "REGIONAL",
 *     },
 *     regionalCertificateName: "example-api",
 * });
 * // Example DNS record using Route53.
 * // Route53 is not specifically required; any DNS host can be used.
 * const exampleRecord = new aws.route53.Record("example", {
 *     aliases: [{
 *         evaluateTargetHealth: true,
 *         name: exampleDomainName.regionalDomainName,
 *         zoneId: exampleDomainName.regionalZoneId,
 *     }],
 *     type: "A",
 *     zoneId: aws_route53_zone_example.id,
 * });
 * ```
 */
export class DomainName extends pulumi.CustomResource {
    /**
     * Get an existing DomainName resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainNameState, opts?: pulumi.CustomResourceOptions): DomainName {
        return new DomainName(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<DomainNameResult> {
        return ctx.list({...args, type: 'aws:apigateway/domainName:DomainName'});
    }

    public static addAdmissionPolicy(policy: pulumi.policy.AdmissionPolicy): void {
        pulumi.runtime.addAdmissionPolicy({
            ...policy,
            pulumiType: 'aws:apigateway/domainName:DomainName',
        });
    }
    /**
     * The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
     */
    public readonly certificateArn: pulumi.Output<string | undefined>;
    /**
     * The certificate issued for the domain name
     * being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
     * `regional_certificate_name`.
     */
    public readonly certificateBody: pulumi.Output<string | undefined>;
    /**
     * The certificate for the CA that issued the
     * certificate, along with any intermediate CA certificates required to
     * create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
     * `regional_certificate_arn`, and `regional_certificate_name`.
     */
    public readonly certificateChain: pulumi.Output<string | undefined>;
    /**
     * The unique name to use when registering this
     * certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
     * `regional_certificate_name`. Required if `certificate_arn` is not set.
     */
    public readonly certificateName: pulumi.Output<string | undefined>;
    /**
     * The private key associated with the
     * domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
     */
    public readonly certificatePrivateKey: pulumi.Output<string | undefined>;
    /**
     * The upload date associated with the domain certificate.
     */
    public /*out*/ readonly certificateUploadDate: pulumi.Output<string>;
    /**
     * The hostname created by Cloudfront to represent
     * the distribution that implements this domain name mapping.
     */
    public /*out*/ readonly cloudfrontDomainName: pulumi.Output<string>;
    /**
     * For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
     * that can be used to create a Route53 alias record for the distribution.
     */
    public /*out*/ readonly cloudfrontZoneId: pulumi.Output<string>;
    /**
     * The fully-qualified domain name to register
     */
    public readonly domainName: pulumi.Output<string>;
    /**
     * Configuration block defining API endpoint information including type. Defined below.
     */
    public readonly endpointConfiguration: pulumi.Output<{ types: string }>;
    /**
     * The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
     */
    public readonly regionalCertificateArn: pulumi.Output<string | undefined>;
    /**
     * The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
     * `certificate_private_key`.
     */
    public readonly regionalCertificateName: pulumi.Output<string | undefined>;
    /**
     * The hostname for the custom domain's regional endpoint.
     */
    public /*out*/ readonly regionalDomainName: pulumi.Output<string>;
    /**
     * The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
     */
    public /*out*/ readonly regionalZoneId: pulumi.Output<string>;

    /**
     * Create a DomainName resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DomainNameArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DomainNameArgs | DomainNameState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: DomainNameState = argsOrState as DomainNameState | undefined;
            inputs["certificateArn"] = state ? state.certificateArn : undefined;
            inputs["certificateBody"] = state ? state.certificateBody : undefined;
            inputs["certificateChain"] = state ? state.certificateChain : undefined;
            inputs["certificateName"] = state ? state.certificateName : undefined;
            inputs["certificatePrivateKey"] = state ? state.certificatePrivateKey : undefined;
            inputs["certificateUploadDate"] = state ? state.certificateUploadDate : undefined;
            inputs["cloudfrontDomainName"] = state ? state.cloudfrontDomainName : undefined;
            inputs["cloudfrontZoneId"] = state ? state.cloudfrontZoneId : undefined;
            inputs["domainName"] = state ? state.domainName : undefined;
            inputs["endpointConfiguration"] = state ? state.endpointConfiguration : undefined;
            inputs["regionalCertificateArn"] = state ? state.regionalCertificateArn : undefined;
            inputs["regionalCertificateName"] = state ? state.regionalCertificateName : undefined;
            inputs["regionalDomainName"] = state ? state.regionalDomainName : undefined;
            inputs["regionalZoneId"] = state ? state.regionalZoneId : undefined;
        } else {
            const args = argsOrState as DomainNameArgs | undefined;
            if (!args || args.domainName === undefined) {
                throw new Error("Missing required property 'domainName'");
            }
            inputs["certificateArn"] = args ? args.certificateArn : undefined;
            inputs["certificateBody"] = args ? args.certificateBody : undefined;
            inputs["certificateChain"] = args ? args.certificateChain : undefined;
            inputs["certificateName"] = args ? args.certificateName : undefined;
            inputs["certificatePrivateKey"] = args ? args.certificatePrivateKey : undefined;
            inputs["domainName"] = args ? args.domainName : undefined;
            inputs["endpointConfiguration"] = args ? args.endpointConfiguration : undefined;
            inputs["regionalCertificateArn"] = args ? args.regionalCertificateArn : undefined;
            inputs["regionalCertificateName"] = args ? args.regionalCertificateName : undefined;
            inputs["certificateUploadDate"] = undefined /*out*/;
            inputs["cloudfrontDomainName"] = undefined /*out*/;
            inputs["cloudfrontZoneId"] = undefined /*out*/;
            inputs["regionalDomainName"] = undefined /*out*/;
            inputs["regionalZoneId"] = undefined /*out*/;
        }
        super("aws:apigateway/domainName:DomainName", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DomainName resources.
 */
export interface DomainNameState {
    /**
     * The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
     */
    readonly certificateArn?: pulumi.Input<string>;
    /**
     * The certificate issued for the domain name
     * being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
     * `regional_certificate_name`.
     */
    readonly certificateBody?: pulumi.Input<string>;
    /**
     * The certificate for the CA that issued the
     * certificate, along with any intermediate CA certificates required to
     * create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
     * `regional_certificate_arn`, and `regional_certificate_name`.
     */
    readonly certificateChain?: pulumi.Input<string>;
    /**
     * The unique name to use when registering this
     * certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
     * `regional_certificate_name`. Required if `certificate_arn` is not set.
     */
    readonly certificateName?: pulumi.Input<string>;
    /**
     * The private key associated with the
     * domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
     */
    readonly certificatePrivateKey?: pulumi.Input<string>;
    /**
     * The upload date associated with the domain certificate.
     */
    readonly certificateUploadDate?: pulumi.Input<string>;
    /**
     * The hostname created by Cloudfront to represent
     * the distribution that implements this domain name mapping.
     */
    readonly cloudfrontDomainName?: pulumi.Input<string>;
    /**
     * For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
     * that can be used to create a Route53 alias record for the distribution.
     */
    readonly cloudfrontZoneId?: pulumi.Input<string>;
    /**
     * The fully-qualified domain name to register
     */
    readonly domainName?: pulumi.Input<string>;
    /**
     * Configuration block defining API endpoint information including type. Defined below.
     */
    readonly endpointConfiguration?: pulumi.Input<{ types: pulumi.Input<string> }>;
    /**
     * The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
     */
    readonly regionalCertificateArn?: pulumi.Input<string>;
    /**
     * The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
     * `certificate_private_key`.
     */
    readonly regionalCertificateName?: pulumi.Input<string>;
    /**
     * The hostname for the custom domain's regional endpoint.
     */
    readonly regionalDomainName?: pulumi.Input<string>;
    /**
     * The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
     */
    readonly regionalZoneId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DomainName resource.
 */
export interface DomainNameArgs {
    /**
     * The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
     */
    readonly certificateArn?: pulumi.Input<string>;
    /**
     * The certificate issued for the domain name
     * being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
     * `regional_certificate_name`.
     */
    readonly certificateBody?: pulumi.Input<string>;
    /**
     * The certificate for the CA that issued the
     * certificate, along with any intermediate CA certificates required to
     * create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
     * `regional_certificate_arn`, and `regional_certificate_name`.
     */
    readonly certificateChain?: pulumi.Input<string>;
    /**
     * The unique name to use when registering this
     * certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
     * `regional_certificate_name`. Required if `certificate_arn` is not set.
     */
    readonly certificateName?: pulumi.Input<string>;
    /**
     * The private key associated with the
     * domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
     */
    readonly certificatePrivateKey?: pulumi.Input<string>;
    /**
     * The fully-qualified domain name to register
     */
    readonly domainName: pulumi.Input<string>;
    /**
     * Configuration block defining API endpoint information including type. Defined below.
     */
    readonly endpointConfiguration?: pulumi.Input<{ types: pulumi.Input<string> }>;
    /**
     * The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
     */
    readonly regionalCertificateArn?: pulumi.Input<string>;
    /**
     * The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
     * `certificate_private_key`.
     */
    readonly regionalCertificateName?: pulumi.Input<string>;
}

/**
 * The live DomainName resource.
 */
export interface DomainNameResult {
    /**
     * The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
     */
    readonly certificateArn?: string;
    /**
     * The certificate issued for the domain name
     * being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
     * `regional_certificate_name`.
     */
    readonly certificateBody?: string;
    /**
     * The certificate for the CA that issued the
     * certificate, along with any intermediate CA certificates required to
     * create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
     * `regional_certificate_arn`, and `regional_certificate_name`.
     */
    readonly certificateChain?: string;
    /**
     * The unique name to use when registering this
     * certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
     * `regional_certificate_name`. Required if `certificate_arn` is not set.
     */
    readonly certificateName?: string;
    /**
     * The private key associated with the
     * domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
     */
    readonly certificatePrivateKey?: string;
    /**
     * The upload date associated with the domain certificate.
     */
    readonly certificateUploadDate: string;
    /**
     * The hostname created by Cloudfront to represent
     * the distribution that implements this domain name mapping.
     */
    readonly cloudfrontDomainName: string;
    /**
     * For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
     * that can be used to create a Route53 alias record for the distribution.
     */
    readonly cloudfrontZoneId: string;
    /**
     * The fully-qualified domain name to register
     */
    readonly domainName: string;
    /**
     * Configuration block defining API endpoint information including type. Defined below.
     */
    readonly endpointConfiguration: { types: string };
    /**
     * The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
     */
    readonly regionalCertificateArn?: string;
    /**
     * The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
     * `certificate_private_key`.
     */
    readonly regionalCertificateName?: string;
    /**
     * The hostname for the custom domain's regional endpoint.
     */
    readonly regionalDomainName: string;
    /**
     * The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
     */
    readonly regionalZoneId: string;
}
