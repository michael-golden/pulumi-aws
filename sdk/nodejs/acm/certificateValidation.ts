// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputApi from "../types/input";
import * as outputApi from "../types/output";
import * as utilities from "../utilities";

/**
 * This resource represents a successful validation of an ACM certificate in concert
 * with other resources.
 * 
 * Most commonly, this resource is used together with `aws.route53.Record` and
 * `aws.acm.Certificate` to request a DNS validated certificate,
 * deploy the required validation records and wait for validation to complete.
 * 
 * > **WARNING:** This resource implements a part of the validation workflow. It does not represent a real-world entity in AWS, therefore changing or deleting this resource on its own has no immediate effect.
 * 
 * 
 * ## Example Usage
 * 
 * ### DNS Validation with Route 53
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const certCertificate = new aws.acm.Certificate("cert", {
 *     domainName: "example.com",
 *     validationMethod: "DNS",
 * });
 * const zone = pulumi.output(aws.route53.getZone({
 *     name: "example.com.",
 *     privateZone: false,
 * }));
 * const certValidation = new aws.route53.Record("certValidation", {
 *     records: [certCertificate.domainValidationOptions[0].resourceRecordValue],
 *     ttl: 60,
 *     type: certCertificate.domainValidationOptions[0].resourceRecordType,
 *     zoneId: zone.id,
 * });
 * const certCertificateValidation = new aws.acm.CertificateValidation("cert", {
 *     certificateArn: certCertificate.arn,
 *     validationRecordFqdns: [certValidation.fqdn],
 * });
 * const frontEnd = new aws.lb.Listener("frontEnd", {
 *     // [...]
 *     certificateArn: certCertificateValidation.certificateArn,
 * });
 * ```
 * 
 * ### Alternative Domains DNS Validation with Route 53
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const certCertificate = new aws.acm.Certificate("cert", {
 *     domainName: "example.com",
 *     subjectAlternativeNames: [
 *         "www.example.com",
 *         "example.org",
 *     ],
 *     validationMethod: "DNS",
 * });
 * const zone = pulumi.output(aws.route53.getZone({
 *     name: "example.com.",
 *     privateZone: false,
 * }));
 * const zoneAlt = pulumi.output(aws.route53.getZone({
 *     name: "example.org.",
 *     privateZone: false,
 * }));
 * const certValidation = new aws.route53.Record("certValidation", {
 *     records: [certCertificate.domainValidationOptions[0].resourceRecordValue],
 *     ttl: 60,
 *     type: certCertificate.domainValidationOptions[0].resourceRecordType,
 *     zoneId: zone.id,
 * });
 * const certValidationAlt1 = new aws.route53.Record("certValidationAlt1", {
 *     records: [certCertificate.domainValidationOptions[1].resourceRecordValue],
 *     ttl: 60,
 *     type: certCertificate.domainValidationOptions[1].resourceRecordType,
 *     zoneId: zone.id,
 * });
 * const certValidationAlt2 = new aws.route53.Record("certValidationAlt2", {
 *     records: [certCertificate.domainValidationOptions[2].resourceRecordValue],
 *     ttl: 60,
 *     type: certCertificate.domainValidationOptions[2].resourceRecordType,
 *     zoneId: zoneAlt.id,
 * });
 * const certCertificateValidation = new aws.acm.CertificateValidation("cert", {
 *     certificateArn: certCertificate.arn,
 *     validationRecordFqdns: [
 *         certValidation.fqdn,
 *         certValidationAlt1.fqdn,
 *         certValidationAlt2.fqdn,
 *     ],
 * });
 * const frontEnd = new aws.lb.Listener("frontEnd", {
 *     // [...]
 *     certificateArn: certCertificateValidation.certificateArn,
 * });
 * ```
 * 
 * ### Email Validation
 * 
 * In this situation, the resource is simply a waiter for manual email approval of ACM certificates.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const certCertificate = new aws.acm.Certificate("cert", {
 *     domainName: "example.com",
 *     validationMethod: "EMAIL",
 * });
 * const certCertificateValidation = new aws.acm.CertificateValidation("cert", {
 *     certificateArn: certCertificate.arn,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/acm_certificate_validation.html.markdown.
 */
export class CertificateValidation extends pulumi.CustomResource {
    /**
     * Get an existing CertificateValidation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertificateValidationState, opts?: pulumi.CustomResourceOptions): CertificateValidation {
        return new CertificateValidation(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:acm/certificateValidation:CertificateValidation';

    /**
     * Returns true if the given object is an instance of CertificateValidation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CertificateValidation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CertificateValidation.__pulumiType;
    }

    /**
     * The ARN of the certificate that is being validated.
     */
    public readonly certificateArn!: pulumi.Output<string>;
    /**
     * List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation
     */
    public readonly validationRecordFqdns!: pulumi.Output<string[] | undefined>;

    /**
     * Create a CertificateValidation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CertificateValidationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CertificateValidationArgs | CertificateValidationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as CertificateValidationState | undefined;
            inputs["certificateArn"] = state ? state.certificateArn : undefined;
            inputs["validationRecordFqdns"] = state ? state.validationRecordFqdns : undefined;
        } else {
            const args = argsOrState as CertificateValidationArgs | undefined;
            if (!args || args.certificateArn === undefined) {
                throw new Error("Missing required property 'certificateArn'");
            }
            inputs["certificateArn"] = args ? args.certificateArn : undefined;
            inputs["validationRecordFqdns"] = args ? args.validationRecordFqdns : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(CertificateValidation.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CertificateValidation resources.
 */
export interface CertificateValidationState {
    /**
     * The ARN of the certificate that is being validated.
     */
    readonly certificateArn?: pulumi.Input<string>;
    /**
     * List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation
     */
    readonly validationRecordFqdns?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a CertificateValidation resource.
 */
export interface CertificateValidationArgs {
    /**
     * The ARN of the certificate that is being validated.
     */
    readonly certificateArn: pulumi.Input<string>;
    /**
     * List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation
     */
    readonly validationRecordFqdns?: pulumi.Input<pulumi.Input<string>[]>;
}
