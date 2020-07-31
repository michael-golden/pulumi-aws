// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Creates an Amazon CloudFront web distribution.
 *
 * For information about CloudFront distributions, see the
 * [Amazon CloudFront Developer Guide](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html). For specific information about creating
 * CloudFront web distributions, see the [POST Distribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html) page in the Amazon
 * CloudFront API Reference.
 *
 * > **NOTE:** CloudFront distributions take about 15 minutes to a deployed state
 * after creation or modification. During this time, deletes to resources will be
 * blocked. If you need to delete a distribution that is enabled and you do not
 * want to wait, you need to use the `retainOnDelete` flag.
 *
 * ## Example Usage
 *
 * The following example below creates a CloudFront distribution with an S3 origin.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const bucket = new aws.s3.Bucket("bucket", {
 *     acl: "private",
 *     tags: {
 *         Name: "My bucket",
 *     },
 * });
 * const s3OriginId = "myS3Origin";
 * const s3Distribution = new aws.cloudfront.Distribution("s3Distribution", {
 *     origins: [{
 *         domainName: bucket.bucketRegionalDomainName,
 *         originId: s3OriginId,
 *         s3OriginConfig: {
 *             originAccessIdentity: "origin-access-identity/cloudfront/ABCDEFG1234567",
 *         },
 *     }],
 *     enabled: true,
 *     isIpv6Enabled: true,
 *     comment: "Some comment",
 *     defaultRootObject: "index.html",
 *     loggingConfig: {
 *         includeCookies: false,
 *         bucket: "mylogs.s3.amazonaws.com",
 *         prefix: "myprefix",
 *     },
 *     aliases: [
 *         "mysite.example.com",
 *         "yoursite.example.com",
 *     ],
 *     defaultCacheBehavior: {
 *         allowedMethods: [
 *             "DELETE",
 *             "GET",
 *             "HEAD",
 *             "OPTIONS",
 *             "PATCH",
 *             "POST",
 *             "PUT",
 *         ],
 *         cachedMethods: [
 *             "GET",
 *             "HEAD",
 *         ],
 *         targetOriginId: s3OriginId,
 *         forwardedValues: {
 *             queryString: false,
 *             cookies: {
 *                 forward: "none",
 *             },
 *         },
 *         viewerProtocolPolicy: "allow-all",
 *         minTtl: 0,
 *         defaultTtl: 3600,
 *         maxTtl: 86400,
 *     },
 *     orderedCacheBehaviors: [
 *         {
 *             pathPattern: "/content/immutable/*",
 *             allowedMethods: [
 *                 "GET",
 *                 "HEAD",
 *                 "OPTIONS",
 *             ],
 *             cachedMethods: [
 *                 "GET",
 *                 "HEAD",
 *                 "OPTIONS",
 *             ],
 *             targetOriginId: s3OriginId,
 *             forwardedValues: {
 *                 queryString: false,
 *                 headers: ["Origin"],
 *                 cookies: {
 *                     forward: "none",
 *                 },
 *             },
 *             minTtl: 0,
 *             defaultTtl: 86400,
 *             maxTtl: 31536000,
 *             compress: true,
 *             viewerProtocolPolicy: "redirect-to-https",
 *         },
 *         {
 *             pathPattern: "/content/*",
 *             allowedMethods: [
 *                 "GET",
 *                 "HEAD",
 *                 "OPTIONS",
 *             ],
 *             cachedMethods: [
 *                 "GET",
 *                 "HEAD",
 *             ],
 *             targetOriginId: s3OriginId,
 *             forwardedValues: {
 *                 queryString: false,
 *                 cookies: {
 *                     forward: "none",
 *                 },
 *             },
 *             minTtl: 0,
 *             defaultTtl: 3600,
 *             maxTtl: 86400,
 *             compress: true,
 *             viewerProtocolPolicy: "redirect-to-https",
 *         },
 *     ],
 *     priceClass: "PriceClass_200",
 *     restrictions: {
 *         geoRestriction: {
 *             restrictionType: "whitelist",
 *             locations: [
 *                 "US",
 *                 "CA",
 *                 "GB",
 *                 "DE",
 *             ],
 *         },
 *     },
 *     tags: {
 *         Environment: "production",
 *     },
 *     viewerCertificate: {
 *         cloudfrontDefaultCertificate: true,
 *     },
 * });
 * ```
 *
 * The following example below creates a Cloudfront distribution with an origin group for failover routing:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const s3Distribution = new aws.cloudfront.Distribution("s3Distribution", {
 *     originGroups: [{
 *         originId: "groupS3",
 *         failoverCriteria: {
 *             statusCodes: [
 *                 403,
 *                 404,
 *                 500,
 *                 502,
 *             ],
 *         },
 *         members: [
 *             {
 *                 originId: "primaryS3",
 *             },
 *             {
 *                 originId: "failoverS3",
 *             },
 *         ],
 *     }],
 *     origins: [
 *         {
 *             domainName: aws_s3_bucket.primary.bucket_regional_domain_name,
 *             originId: "primaryS3",
 *             s3OriginConfig: {
 *                 originAccessIdentity: aws_cloudfront_origin_access_identity["default"].cloudfront_access_identity_path,
 *             },
 *         },
 *         {
 *             domainName: aws_s3_bucket.failover.bucket_regional_domain_name,
 *             originId: "failoverS3",
 *             s3OriginConfig: {
 *                 originAccessIdentity: aws_cloudfront_origin_access_identity["default"].cloudfront_access_identity_path,
 *             },
 *         },
 *     ],
 *     defaultCacheBehavior: {
 *         targetOriginId: "groupS3",
 *     },
 * });
 * // ... other configuration ...
 * ```
 */
export class Distribution extends pulumi.CustomResource {
    /**
     * Get an existing Distribution resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DistributionState, opts?: pulumi.CustomResourceOptions): Distribution {
        return new Distribution(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:cloudfront/distribution:Distribution';

    /**
     * Returns true if the given object is an instance of Distribution.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Distribution {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Distribution.__pulumiType;
    }

    /**
     * Extra CNAMEs (alternate domain names), if any, for
     * this distribution.
     */
    public readonly aliases!: pulumi.Output<string[] | undefined>;
    /**
     * The ARN (Amazon Resource Name) for the distribution. For example: `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where `123456789012` is your AWS account ID.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Internal value used by CloudFront to allow future
     * updates to the distribution configuration.
     */
    public /*out*/ readonly callerReference!: pulumi.Output<string>;
    /**
     * Any comments you want to include about the
     * distribution.
     */
    public readonly comment!: pulumi.Output<string | undefined>;
    /**
     * One or more custom error response elements (multiples allowed).
     */
    public readonly customErrorResponses!: pulumi.Output<outputs.cloudfront.DistributionCustomErrorResponse[] | undefined>;
    /**
     * The default cache behavior for this distribution (maximum
     * one).
     */
    public readonly defaultCacheBehavior!: pulumi.Output<outputs.cloudfront.DistributionDefaultCacheBehavior>;
    /**
     * The object that you want CloudFront to
     * return (for example, index.html) when an end user requests the root URL.
     */
    public readonly defaultRootObject!: pulumi.Output<string | undefined>;
    /**
     * The DNS domain name of either the S3 bucket, or
     * web site of your custom origin.
     */
    public /*out*/ readonly domainName!: pulumi.Output<string>;
    /**
     * Whether the distribution is enabled to accept end
     * user requests for content.
     */
    public readonly enabled!: pulumi.Output<boolean>;
    /**
     * The current version of the distribution's information. For example:
     * `E2QWRUHAPOMQZL`.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    /**
     * The CloudFront Route 53 zone ID that can be used to
     * route an [Alias Resource Record Set](http://docs.aws.amazon.com/Route53/latest/APIReference/CreateAliasRRSAPI.html) to. This attribute is simply an
     * alias for the zone ID `Z2FDTNDATAQYW2`.
     */
    public /*out*/ readonly hostedZoneId!: pulumi.Output<string>;
    /**
     * The maximum HTTP version to support on the
     * distribution. Allowed values are `http1.1` and `http2`. The default is
     * `http2`.
     */
    public readonly httpVersion!: pulumi.Output<string | undefined>;
    /**
     * The number of invalidation batches
     * currently in progress.
     */
    public /*out*/ readonly inProgressValidationBatches!: pulumi.Output<number>;
    /**
     * Whether the IPv6 is enabled for the distribution.
     */
    public readonly isIpv6Enabled!: pulumi.Output<boolean | undefined>;
    /**
     * The date and time the distribution was last modified.
     */
    public /*out*/ readonly lastModifiedTime!: pulumi.Output<string>;
    /**
     * The logging
     * configuration that controls how logs are written
     * to your distribution (maximum one).
     */
    public readonly loggingConfig!: pulumi.Output<outputs.cloudfront.DistributionLoggingConfig | undefined>;
    /**
     * An ordered list of cache behaviors
     * resource for this distribution. List from top to bottom
     * in order of precedence. The topmost cache behavior will have precedence 0.
     */
    public readonly orderedCacheBehaviors!: pulumi.Output<outputs.cloudfront.DistributionOrderedCacheBehavior[] | undefined>;
    /**
     * One or more originGroup for this
     * distribution (multiples allowed).
     */
    public readonly originGroups!: pulumi.Output<outputs.cloudfront.DistributionOriginGroup[] | undefined>;
    /**
     * One or more origins for this
     * distribution (multiples allowed).
     */
    public readonly origins!: pulumi.Output<outputs.cloudfront.DistributionOrigin[]>;
    /**
     * The price class for this distribution. One of
     * `PriceClass_All`, `PriceClass_200`, `PriceClass_100`
     */
    public readonly priceClass!: pulumi.Output<string | undefined>;
    /**
     * The restriction
     * configuration for this distribution (maximum one).
     */
    public readonly restrictions!: pulumi.Output<outputs.cloudfront.DistributionRestrictions>;
    /**
     * Disables the distribution instead of
     * deleting it when destroying the resource. If this is set,
     * the distribution needs to be deleted manually afterwards. Default: `false`.
     */
    public readonly retainOnDelete!: pulumi.Output<boolean | undefined>;
    /**
     * The current status of the distribution. `Deployed` if the
     * distribution's information is fully propagated throughout the Amazon
     * CloudFront system.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * A map of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * List of AWS account IDs (or `self`) that you want to allow to create signed URLs for private content. 
     * See the [CloudFront User Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html) for more information about this feature.
     */
    public /*out*/ readonly trustedSigners!: pulumi.Output<outputs.cloudfront.DistributionTrustedSigner[]>;
    /**
     * The SSL
     * configuration for this distribution (maximum
     * one).
     */
    public readonly viewerCertificate!: pulumi.Output<outputs.cloudfront.DistributionViewerCertificate>;
    /**
     * If enabled, the resource will wait for
     * the distribution status to change from `InProgress` to `Deployed`. Setting
     * this to`false` will skip the process. Default: `true`.
     */
    public readonly waitForDeployment!: pulumi.Output<boolean | undefined>;
    /**
     * If you're using AWS WAF to filter CloudFront
     * requests, the Id of the AWS WAF web ACL that is associated with the
     * distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
     * region and the credentials configuring this argument must have
     * `waf:GetWebACL` permissions assigned. If using WAFv2, provide the ARN of the web ACL.
     */
    public readonly webAclId!: pulumi.Output<string | undefined>;

    /**
     * Create a Distribution resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DistributionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DistributionArgs | DistributionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DistributionState | undefined;
            inputs["aliases"] = state ? state.aliases : undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["callerReference"] = state ? state.callerReference : undefined;
            inputs["comment"] = state ? state.comment : undefined;
            inputs["customErrorResponses"] = state ? state.customErrorResponses : undefined;
            inputs["defaultCacheBehavior"] = state ? state.defaultCacheBehavior : undefined;
            inputs["defaultRootObject"] = state ? state.defaultRootObject : undefined;
            inputs["domainName"] = state ? state.domainName : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["hostedZoneId"] = state ? state.hostedZoneId : undefined;
            inputs["httpVersion"] = state ? state.httpVersion : undefined;
            inputs["inProgressValidationBatches"] = state ? state.inProgressValidationBatches : undefined;
            inputs["isIpv6Enabled"] = state ? state.isIpv6Enabled : undefined;
            inputs["lastModifiedTime"] = state ? state.lastModifiedTime : undefined;
            inputs["loggingConfig"] = state ? state.loggingConfig : undefined;
            inputs["orderedCacheBehaviors"] = state ? state.orderedCacheBehaviors : undefined;
            inputs["originGroups"] = state ? state.originGroups : undefined;
            inputs["origins"] = state ? state.origins : undefined;
            inputs["priceClass"] = state ? state.priceClass : undefined;
            inputs["restrictions"] = state ? state.restrictions : undefined;
            inputs["retainOnDelete"] = state ? state.retainOnDelete : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["trustedSigners"] = state ? state.trustedSigners : undefined;
            inputs["viewerCertificate"] = state ? state.viewerCertificate : undefined;
            inputs["waitForDeployment"] = state ? state.waitForDeployment : undefined;
            inputs["webAclId"] = state ? state.webAclId : undefined;
        } else {
            const args = argsOrState as DistributionArgs | undefined;
            if (!args || args.defaultCacheBehavior === undefined) {
                throw new Error("Missing required property 'defaultCacheBehavior'");
            }
            if (!args || args.enabled === undefined) {
                throw new Error("Missing required property 'enabled'");
            }
            if (!args || args.origins === undefined) {
                throw new Error("Missing required property 'origins'");
            }
            if (!args || args.restrictions === undefined) {
                throw new Error("Missing required property 'restrictions'");
            }
            if (!args || args.viewerCertificate === undefined) {
                throw new Error("Missing required property 'viewerCertificate'");
            }
            inputs["aliases"] = args ? args.aliases : undefined;
            inputs["comment"] = args ? args.comment : undefined;
            inputs["customErrorResponses"] = args ? args.customErrorResponses : undefined;
            inputs["defaultCacheBehavior"] = args ? args.defaultCacheBehavior : undefined;
            inputs["defaultRootObject"] = args ? args.defaultRootObject : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["httpVersion"] = args ? args.httpVersion : undefined;
            inputs["isIpv6Enabled"] = args ? args.isIpv6Enabled : undefined;
            inputs["loggingConfig"] = args ? args.loggingConfig : undefined;
            inputs["orderedCacheBehaviors"] = args ? args.orderedCacheBehaviors : undefined;
            inputs["originGroups"] = args ? args.originGroups : undefined;
            inputs["origins"] = args ? args.origins : undefined;
            inputs["priceClass"] = args ? args.priceClass : undefined;
            inputs["restrictions"] = args ? args.restrictions : undefined;
            inputs["retainOnDelete"] = args ? args.retainOnDelete : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["viewerCertificate"] = args ? args.viewerCertificate : undefined;
            inputs["waitForDeployment"] = args ? args.waitForDeployment : undefined;
            inputs["webAclId"] = args ? args.webAclId : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["callerReference"] = undefined /*out*/;
            inputs["domainName"] = undefined /*out*/;
            inputs["etag"] = undefined /*out*/;
            inputs["hostedZoneId"] = undefined /*out*/;
            inputs["inProgressValidationBatches"] = undefined /*out*/;
            inputs["lastModifiedTime"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
            inputs["trustedSigners"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Distribution.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Distribution resources.
 */
export interface DistributionState {
    /**
     * Extra CNAMEs (alternate domain names), if any, for
     * this distribution.
     */
    readonly aliases?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ARN (Amazon Resource Name) for the distribution. For example: `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where `123456789012` is your AWS account ID.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * Internal value used by CloudFront to allow future
     * updates to the distribution configuration.
     */
    readonly callerReference?: pulumi.Input<string>;
    /**
     * Any comments you want to include about the
     * distribution.
     */
    readonly comment?: pulumi.Input<string>;
    /**
     * One or more custom error response elements (multiples allowed).
     */
    readonly customErrorResponses?: pulumi.Input<pulumi.Input<inputs.cloudfront.DistributionCustomErrorResponse>[]>;
    /**
     * The default cache behavior for this distribution (maximum
     * one).
     */
    readonly defaultCacheBehavior?: pulumi.Input<inputs.cloudfront.DistributionDefaultCacheBehavior>;
    /**
     * The object that you want CloudFront to
     * return (for example, index.html) when an end user requests the root URL.
     */
    readonly defaultRootObject?: pulumi.Input<string>;
    /**
     * The DNS domain name of either the S3 bucket, or
     * web site of your custom origin.
     */
    readonly domainName?: pulumi.Input<string>;
    /**
     * Whether the distribution is enabled to accept end
     * user requests for content.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The current version of the distribution's information. For example:
     * `E2QWRUHAPOMQZL`.
     */
    readonly etag?: pulumi.Input<string>;
    /**
     * The CloudFront Route 53 zone ID that can be used to
     * route an [Alias Resource Record Set](http://docs.aws.amazon.com/Route53/latest/APIReference/CreateAliasRRSAPI.html) to. This attribute is simply an
     * alias for the zone ID `Z2FDTNDATAQYW2`.
     */
    readonly hostedZoneId?: pulumi.Input<string>;
    /**
     * The maximum HTTP version to support on the
     * distribution. Allowed values are `http1.1` and `http2`. The default is
     * `http2`.
     */
    readonly httpVersion?: pulumi.Input<string>;
    /**
     * The number of invalidation batches
     * currently in progress.
     */
    readonly inProgressValidationBatches?: pulumi.Input<number>;
    /**
     * Whether the IPv6 is enabled for the distribution.
     */
    readonly isIpv6Enabled?: pulumi.Input<boolean>;
    /**
     * The date and time the distribution was last modified.
     */
    readonly lastModifiedTime?: pulumi.Input<string>;
    /**
     * The logging
     * configuration that controls how logs are written
     * to your distribution (maximum one).
     */
    readonly loggingConfig?: pulumi.Input<inputs.cloudfront.DistributionLoggingConfig>;
    /**
     * An ordered list of cache behaviors
     * resource for this distribution. List from top to bottom
     * in order of precedence. The topmost cache behavior will have precedence 0.
     */
    readonly orderedCacheBehaviors?: pulumi.Input<pulumi.Input<inputs.cloudfront.DistributionOrderedCacheBehavior>[]>;
    /**
     * One or more originGroup for this
     * distribution (multiples allowed).
     */
    readonly originGroups?: pulumi.Input<pulumi.Input<inputs.cloudfront.DistributionOriginGroup>[]>;
    /**
     * One or more origins for this
     * distribution (multiples allowed).
     */
    readonly origins?: pulumi.Input<pulumi.Input<inputs.cloudfront.DistributionOrigin>[]>;
    /**
     * The price class for this distribution. One of
     * `PriceClass_All`, `PriceClass_200`, `PriceClass_100`
     */
    readonly priceClass?: pulumi.Input<string>;
    /**
     * The restriction
     * configuration for this distribution (maximum one).
     */
    readonly restrictions?: pulumi.Input<inputs.cloudfront.DistributionRestrictions>;
    /**
     * Disables the distribution instead of
     * deleting it when destroying the resource. If this is set,
     * the distribution needs to be deleted manually afterwards. Default: `false`.
     */
    readonly retainOnDelete?: pulumi.Input<boolean>;
    /**
     * The current status of the distribution. `Deployed` if the
     * distribution's information is fully propagated throughout the Amazon
     * CloudFront system.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * A map of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * List of AWS account IDs (or `self`) that you want to allow to create signed URLs for private content. 
     * See the [CloudFront User Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html) for more information about this feature.
     */
    readonly trustedSigners?: pulumi.Input<pulumi.Input<inputs.cloudfront.DistributionTrustedSigner>[]>;
    /**
     * The SSL
     * configuration for this distribution (maximum
     * one).
     */
    readonly viewerCertificate?: pulumi.Input<inputs.cloudfront.DistributionViewerCertificate>;
    /**
     * If enabled, the resource will wait for
     * the distribution status to change from `InProgress` to `Deployed`. Setting
     * this to`false` will skip the process. Default: `true`.
     */
    readonly waitForDeployment?: pulumi.Input<boolean>;
    /**
     * If you're using AWS WAF to filter CloudFront
     * requests, the Id of the AWS WAF web ACL that is associated with the
     * distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
     * region and the credentials configuring this argument must have
     * `waf:GetWebACL` permissions assigned. If using WAFv2, provide the ARN of the web ACL.
     */
    readonly webAclId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Distribution resource.
 */
export interface DistributionArgs {
    /**
     * Extra CNAMEs (alternate domain names), if any, for
     * this distribution.
     */
    readonly aliases?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Any comments you want to include about the
     * distribution.
     */
    readonly comment?: pulumi.Input<string>;
    /**
     * One or more custom error response elements (multiples allowed).
     */
    readonly customErrorResponses?: pulumi.Input<pulumi.Input<inputs.cloudfront.DistributionCustomErrorResponse>[]>;
    /**
     * The default cache behavior for this distribution (maximum
     * one).
     */
    readonly defaultCacheBehavior: pulumi.Input<inputs.cloudfront.DistributionDefaultCacheBehavior>;
    /**
     * The object that you want CloudFront to
     * return (for example, index.html) when an end user requests the root URL.
     */
    readonly defaultRootObject?: pulumi.Input<string>;
    /**
     * Whether the distribution is enabled to accept end
     * user requests for content.
     */
    readonly enabled: pulumi.Input<boolean>;
    /**
     * The maximum HTTP version to support on the
     * distribution. Allowed values are `http1.1` and `http2`. The default is
     * `http2`.
     */
    readonly httpVersion?: pulumi.Input<string>;
    /**
     * Whether the IPv6 is enabled for the distribution.
     */
    readonly isIpv6Enabled?: pulumi.Input<boolean>;
    /**
     * The logging
     * configuration that controls how logs are written
     * to your distribution (maximum one).
     */
    readonly loggingConfig?: pulumi.Input<inputs.cloudfront.DistributionLoggingConfig>;
    /**
     * An ordered list of cache behaviors
     * resource for this distribution. List from top to bottom
     * in order of precedence. The topmost cache behavior will have precedence 0.
     */
    readonly orderedCacheBehaviors?: pulumi.Input<pulumi.Input<inputs.cloudfront.DistributionOrderedCacheBehavior>[]>;
    /**
     * One or more originGroup for this
     * distribution (multiples allowed).
     */
    readonly originGroups?: pulumi.Input<pulumi.Input<inputs.cloudfront.DistributionOriginGroup>[]>;
    /**
     * One or more origins for this
     * distribution (multiples allowed).
     */
    readonly origins: pulumi.Input<pulumi.Input<inputs.cloudfront.DistributionOrigin>[]>;
    /**
     * The price class for this distribution. One of
     * `PriceClass_All`, `PriceClass_200`, `PriceClass_100`
     */
    readonly priceClass?: pulumi.Input<string>;
    /**
     * The restriction
     * configuration for this distribution (maximum one).
     */
    readonly restrictions: pulumi.Input<inputs.cloudfront.DistributionRestrictions>;
    /**
     * Disables the distribution instead of
     * deleting it when destroying the resource. If this is set,
     * the distribution needs to be deleted manually afterwards. Default: `false`.
     */
    readonly retainOnDelete?: pulumi.Input<boolean>;
    /**
     * A map of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The SSL
     * configuration for this distribution (maximum
     * one).
     */
    readonly viewerCertificate: pulumi.Input<inputs.cloudfront.DistributionViewerCertificate>;
    /**
     * If enabled, the resource will wait for
     * the distribution status to change from `InProgress` to `Deployed`. Setting
     * this to`false` will skip the process. Default: `true`.
     */
    readonly waitForDeployment?: pulumi.Input<boolean>;
    /**
     * If you're using AWS WAF to filter CloudFront
     * requests, the Id of the AWS WAF web ACL that is associated with the
     * distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
     * region and the credentials configuring this argument must have
     * `waf:GetWebACL` permissions assigned. If using WAFv2, provide the ARN of the web ACL.
     */
    readonly webAclId?: pulumi.Input<string>;
}
